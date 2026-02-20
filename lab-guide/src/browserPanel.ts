import * as vscode from 'vscode';

export class BrowserPanel {
  private panel: vscode.WebviewPanel | undefined;
  private currentUrl: string | undefined;

  constructor(private context: vscode.ExtensionContext) {}

  show(url: string) {
    this.currentUrl = url;

    if (this.panel) {
      this.panel.reveal(vscode.ViewColumn.One);
      this.panel.webview.html = this.getHtml(url);
      return;
    }

    this.panel = vscode.window.createWebviewPanel(
      'labGuide.browser',
      'Course Catalog',
      { viewColumn: vscode.ViewColumn.One, preserveFocus: true },
      {
        enableScripts: true,
        retainContextWhenHidden: true
      }
    );

    this.panel.webview.html = this.getHtml(url);
    this.panel.onDidDispose(() => { this.panel = undefined; });
  }

  navigate(url: string) {
    this.currentUrl = url;
    if (this.panel) {
      // Update the title based on content
      const parts = url.replace(/\/+$/, '').split('/');
      const name = parts[parts.length - 1]?.replace(/-/g, ' ') || 'Course';
      this.panel.title = name;
      this.panel.webview.html = this.getHtml(url);
    } else {
      this.show(url);
    }
  }

  dispose() {
    this.panel?.dispose();
  }

  private getHtml(url: string): string {
    const nonce = getNonce();
    return /*html*/ `<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="Content-Security-Policy"
    content="default-src 'none';
             frame-src https: http:;
             style-src 'nonce-${nonce}';">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <style nonce="${nonce}">
    * { margin: 0; padding: 0; }
    html, body { height: 100%; overflow: hidden; }
    iframe {
      width: 100%;
      height: 100%;
      border: none;
    }
  </style>
</head>
<body>
  <iframe src="${escapeHtml(url)}" sandbox="allow-scripts allow-same-origin allow-forms allow-popups"></iframe>
</body>
</html>`;
  }
}

function getNonce(): string {
  const chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
  let out = '';
  for (let i = 0; i < 32; i++) {
    out += chars.charAt(Math.floor(Math.random() * chars.length));
  }
  return out;
}

function escapeHtml(str: string): string {
  return str.replace(/&/g, '&amp;').replace(/"/g, '&quot;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
}
