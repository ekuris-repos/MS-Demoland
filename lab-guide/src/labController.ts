import * as vscode from 'vscode';
import * as http from 'http';
import * as https from 'https';
import { GuidePanel } from './guidePanel';
import { BrowserPanel } from './browserPanel';

export interface LabStep {
  title: string;
  instruction: string;
  tip?: string;
  focus?: 'slides' | 'chat' | 'terminal' | 'editor' | 'guide';
}

export interface Lab {
  title: string;
  steps: LabStep[];
}

export class LabController {
  private guidePanel: GuidePanel | undefined;
  private browserPanel: BrowserPanel;
  private lab: Lab | undefined;
  private currentStep = 0;
  private statusBarItem: vscode.StatusBarItem;

  constructor(
    private context: vscode.ExtensionContext,
    private log: vscode.LogOutputChannel
  ) {
    this.statusBarItem = vscode.window.createStatusBarItem(vscode.StatusBarAlignment.Left, 100);
    context.subscriptions.push(this.statusBarItem);
    this.browserPanel = new BrowserPanel(context);
  }

  // ── Open catalog in our browser panel ──────────────────────────
  openCatalog(url: string) {
    this.log.info(`openCatalog → ${url}`);
    this.browserPanel.show(url);
  }

  // ── Start lab via URI handler ──────────────────────────────────
  async startLabFromUri(server: string, coursePath: string) {
    server = server.replace(/\/+$/, '');
    coursePath = coursePath.replace(/^\/+|\/+$/g, '');

    const labUrl = `${server}/${coursePath}/lab.json`;
    this.log.info(`Fetching lab → ${labUrl}`);

    vscode.window.withProgress(
      { location: vscode.ProgressLocation.Notification, title: 'Loading lab…' },
      async () => {
        const labJson = await this.fetchJson(labUrl);
        if (!labJson) {
          this.log.error(`Failed to fetch lab from ${labUrl}`);
          vscode.window.showErrorMessage(`Could not load lab from ${labUrl}`);
          return;
        }

        this.lab = labJson as Lab;
        this.currentStep = 0;
        this.log.info(`Lab loaded: "${this.lab.title}" — ${this.lab.steps.length} steps`);

        // Navigate the browser panel to the course slides (left column)
        const courseUrl = `${server}/${coursePath}/`;
        this.log.info(`Navigating browser panel → ${courseUrl}`);
        this.browserPanel.navigate(courseUrl);

        // Open guide panel in column 2 (center)
        if (!this.guidePanel) {
          this.guidePanel = new GuidePanel(this.context, msg => this.onWebviewMessage(msg));
        }
        this.guidePanel.show();
        this.log.info('Guide panel opened');

        this.guidePanel.postMessage({ type: 'setTitle', title: this.lab.title });

        this.statusBarItem.show();
        this.showCurrentStep();
      }
    );
  }

  // ── Start lab interactively (command palette) ──────────────────
  async startLab() {
    const catalogUrl = vscode.workspace.getConfiguration('labGuide').get<string>('catalogUrl');
    const defaultUrl = catalogUrl?.replace(/\/+$/, '') || 'https://ekuris-repos.github.io/MS-Demoland';

    const server = await vscode.window.showInputBox({
      title: 'Course Server URL',
      prompt: 'Base URL of the course site',
      value: defaultUrl,
      validateInput: (v) => {
        try { new URL(v); return null; }
        catch { return 'Enter a valid URL'; }
      }
    });

    if (!server) { return; }
    this.log.info(`startLab → opening catalog at ${server}`);
    this.openCatalog(server.replace(/\/+$/, '') + '/');
  }

  nextStep() {
    if (!this.lab || this.currentStep >= this.lab.steps.length - 1) { return; }
    this.currentStep++;
    this.showCurrentStep();
  }

  prevStep() {
    if (!this.lab || this.currentStep <= 0) { return; }
    this.currentStep--;
    this.showCurrentStep();
  }

  reset() {
    this.currentStep = 0;
    if (this.lab) { this.showCurrentStep(); }
  }

  dispose() {
    this.guidePanel?.dispose();
    this.browserPanel.dispose();
    this.statusBarItem.dispose();
  }

  // ── Fetch JSON from a URL ─────────────────────────────────────
  private fetchJson(url: string): Promise<unknown | null> {
    return new Promise((resolve) => {
      const client = url.startsWith('https') ? https : http;
      const req = client.get(url, { timeout: 8000 }, (res) => {
        if (res.statusCode !== 200) {
          resolve(null);
          return;
        }
        let data = '';
        res.on('data', chunk => { data += chunk; });
        res.on('end', () => {
          try { resolve(JSON.parse(data)); }
          catch { resolve(null); }
        });
      });
      req.on('error', () => resolve(null));
      req.on('timeout', () => { req.destroy(); resolve(null); });
    });
  }

  // ── Quick probe to check if a URL is reachable ────────────────
  private probeUrl(url: string): Promise<boolean> {
    return new Promise((resolve) => {
      const client = url.startsWith('https') ? https : http;
      const req = client.get(url, { timeout: 3000 }, (res) => {
        res.resume();
        resolve(res.statusCode !== undefined && res.statusCode < 400);
      });
      req.on('error', () => resolve(false));
      req.on('timeout', () => { req.destroy(); resolve(false); });
    });
  }

  private showCurrentStep() {
    if (!this.lab || !this.guidePanel) { return; }

    const step = this.lab.steps[this.currentStep];
    this.statusBarItem.text = `$(book) Lab: ${this.currentStep + 1}/${this.lab.steps.length} — ${step.title}`;

    this.guidePanel.postMessage({
      type: 'setState',
      step: { ...step, index: this.currentStep, total: this.lab.steps.length }
    });
  }

  private onWebviewMessage(msg: { type: string }) {
    switch (msg.type) {
      case 'nextStep': this.nextStep(); break;
      case 'prevStep': this.prevStep(); break;
      case 'ready': this.showCurrentStep(); break;
    }
  }
}
