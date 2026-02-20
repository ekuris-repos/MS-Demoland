"use strict";
var __createBinding = (this && this.__createBinding) || (Object.create ? (function(o, m, k, k2) {
    if (k2 === undefined) k2 = k;
    var desc = Object.getOwnPropertyDescriptor(m, k);
    if (!desc || ("get" in desc ? !m.__esModule : desc.writable || desc.configurable)) {
      desc = { enumerable: true, get: function() { return m[k]; } };
    }
    Object.defineProperty(o, k2, desc);
}) : (function(o, m, k, k2) {
    if (k2 === undefined) k2 = k;
    o[k2] = m[k];
}));
var __setModuleDefault = (this && this.__setModuleDefault) || (Object.create ? (function(o, v) {
    Object.defineProperty(o, "default", { enumerable: true, value: v });
}) : function(o, v) {
    o["default"] = v;
});
var __importStar = (this && this.__importStar) || (function () {
    var ownKeys = function(o) {
        ownKeys = Object.getOwnPropertyNames || function (o) {
            var ar = [];
            for (var k in o) if (Object.prototype.hasOwnProperty.call(o, k)) ar[ar.length] = k;
            return ar;
        };
        return ownKeys(o);
    };
    return function (mod) {
        if (mod && mod.__esModule) return mod;
        var result = {};
        if (mod != null) for (var k = ownKeys(mod), i = 0; i < k.length; i++) if (k[i] !== "default") __createBinding(result, mod, k[i]);
        __setModuleDefault(result, mod);
        return result;
    };
})();
Object.defineProperty(exports, "__esModule", { value: true });
exports.BrowserPanel = void 0;
const vscode = __importStar(require("vscode"));
class BrowserPanel {
    constructor(context) {
        this.context = context;
    }
    show(url) {
        this.currentUrl = url;
        if (this.panel) {
            this.panel.reveal(vscode.ViewColumn.One);
            this.panel.webview.html = this.getHtml(url);
            return;
        }
        this.panel = vscode.window.createWebviewPanel('labGuide.browser', 'Course Catalog', { viewColumn: vscode.ViewColumn.One, preserveFocus: true }, {
            enableScripts: true,
            retainContextWhenHidden: true
        });
        this.panel.webview.html = this.getHtml(url);
        this.panel.onDidDispose(() => { this.panel = undefined; });
    }
    navigate(url) {
        this.currentUrl = url;
        if (this.panel) {
            // Update the title based on content
            const parts = url.replace(/\/+$/, '').split('/');
            const name = parts[parts.length - 1]?.replace(/-/g, ' ') || 'Course';
            this.panel.title = name;
            this.panel.webview.html = this.getHtml(url);
        }
        else {
            this.show(url);
        }
    }
    dispose() {
        this.panel?.dispose();
    }
    getHtml(url) {
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
exports.BrowserPanel = BrowserPanel;
function getNonce() {
    const chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
    let out = '';
    for (let i = 0; i < 32; i++) {
        out += chars.charAt(Math.floor(Math.random() * chars.length));
    }
    return out;
}
function escapeHtml(str) {
    return str.replace(/&/g, '&amp;').replace(/"/g, '&quot;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
}
//# sourceMappingURL=browserPanel.js.map