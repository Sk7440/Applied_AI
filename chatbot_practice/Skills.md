# UI/UX Design Skill & Guidelines Definition

> **Context**: High-performance UI/UX Specification derived from Modern Conversational AI Interfaces, enhanced with Next-Gen Interactive Features.

---

## 1. Overview & Core Philosophy

This document outlines UI/UX design rules, component hierarchy, visual design tokens, and innovative interaction paradigms for next-generation dark-mode AI applications.

### Core Design Principles
* **Content-Centric Minimalism**: Pitch-black canvas (`#000000`) for OLED power efficiency and visual contrast.
* **Focal Clarity**: Centralized landing zone with contextual awareness to reduce cognitive load.
* **Adaptive Navigation**: Collapsible sidebar with dynamic workspace switching and feature surface controls.

---

## 2. Visual Design System

### A. Color Palette
| Category | Token Name | Hex / Value | Purpose / Usage |
| :--- | :--- | :--- | :--- |
| **Canvas** | `--bg-primary` | `#000000` | Main application background |
| **Surface** | `--bg-secondary` | `#171717` / `#212121` | Sidebar, input pill, floating widgets |
| **Hover Surface** | `--bg-hover` | `#2f2f2f` | Actionable hover highlights |
| **Text Primary** | `--text-primary` | `#ffffff` | Headings, high-priority readable text |
| **Text Muted** | `--text-muted` | `#8e8e93` | Secondary labels, hints, inactive states |
| **Accent Primary**| `--accent-blue` | `#2b7fff` | Real-time audio waveform, active toggles |
| **Accent Glow** | `--accent-glow` | `rgba(43, 127, 255, 0.25)` | Focus state ambient halos |
| **Badge / Status**| `--badge-bg` | `#262626` | Feature badges (`UPDATED`, `Pro`) |

### B. Typography Scale
* **Headline (`H1`)**: `24px / 1.4` (Medium 500)
* **Section Heading (`H2`)**: `18px / 1.3` (Semi-Bold 600)
* **Body / Nav Item**: `14px / 1.4` (Regular 400 - Medium 500)
* **Caption / Badge**: `10px / 1.0` (Bold 700, Upper)

---

## 3. Innovative UI/UX Features (New Additions)

### 1. Dynamic Canvas Spatial Workspace (Mode Switching)
* **Description**: Allows users to split the central workspace seamlessly into dual viewports (e.g., Chat Stream alongside Live Artifact / Web Canvas / Code Sandbox).
* **Interaction**: Hovering over interactive output triggers a smooth 3D split-screen transition (`flex: 1 1 50%` with smooth bezier easing).

### 2. Multi-Modal Context Drawer & Radial Quick Actions
* **Description**: Dragging files or code blocks anywhere onto the screen activates a contextual drop ring overlay centered around the input pill.
* **UX Flow**:
  * Drop into **Top**: "Analyze / Summarize"
  * Drop into **Left**: "Attach to Active Thread"
  * Drop into **Right**: "Convert to Code Canvas"

### 3. Adaptive "Think & Reasoning" Depth Slider
* **Description**: Replaces the binary `Think` button with a micro-slider (`Quick`, `Balanced`, `Deep Reasoning`).
* **Visual Representation**: Mini step-gauge with active glow intensities indicating compute depth before execution.

### 4. Ambient Waveform Audio Visualizer & Spatial Mic
* **Description**: Real-time reactive audio aura surrounding the input pill during voice modes.
* **UX Touch**: Smooth CSS keyframe pulse matching speech amplitude instead of static icons.

### 5. Floating Workspace Command Palette (`Cmd + K`)
* **Description**: Overlay spotlight menu allowing rapid chat searching, project switching, and setting adjustments without navigating the sidebar.

---

## 4. Component Architecture & Specs

### A. Unified Floating Prompt Bar (`.prompt-bar`)
* **Border Radius**: Full Pill (`9999px`)
* **Background**: Surface Secondary (`#212121`) with `1px solid #333333` subtle outline.
* **Layout**:
  1. **Attachment Key (`+`)**: Far-left iconography for contextual uploads.
  2. **Auto-Expanding Input**: Borderless inline textarea auto-growing up to `240px` height.
  3. **Reasoning Gauge**: Integrated multi-level depth toggle.
  4. **Voice & Action Hub**: Voice visualizer button + Send action button.

### B. Collapsible Navigation Sidebar (`.sidebar`)
* **Width**: `260px` collapsed to `64px` icon bar.
* **Sections**:
  1. **Header**: Logo branding, Global Search (`Cmd + K`), Collapse Toggle.
  2. **CTA**: `+ New chat` (Pill button with subtle hover glow).
  3. **Modules**: `Images` (Badge), `Library`, `Scheduled`, `Plugins`, `Projects`.
  4. **Recents Accordion**: Dynamic thread list with drag-and-drop grouping.
  5. **Footer Card**: User profile, tier badge (`Free` / `Pro`), and upgrade callouts.

---

## 5. Interaction & Animation Rules

1. **Focus State**: Focusing the input bar expands ambient background glow (`box-shadow: 0 0 20px var(--accent-glow)`).
2. **Micro-Interactions**: All button hover transitions use `cubic-bezier(0.16, 1, 0.3, 1)` timing over `150ms`.
3. **Keyboard Accessibility**: Full `Tab` key ring navigation with high-contrast indicator focus states.

---

## 6. Implementation Reference

```html
<!-- Enhanced HTML Layout Structure -->
<div class="app-layout">
  <aside class="sidebar">
    <div class="sidebar-header">
      <span class="brand">ChatGPT</span>
      <button class="cmd-k-trigger" title="Command Palette (Cmd + K)"></button>
    </div>
    <button class="btn-new-chat">+ New chat</button>
    <nav class="nav-links">
      <a href="#" class="nav-item">Images <span class="badge">UPDATED</span></a>
      <a href="#" class="nav-item">Canvas Workspace</a>
      <a href="#" class="nav-item">Projects</a>
    </nav>
    <div class="sidebar-footer">
      <div class="user-profile">
        <div class="avatar">SK</div>
        <div class="info">
          <span class="name">Sultan Khalid</span>
          <span class="plan">Pro</span>
        </div>
      </div>
    </div>
  </aside>

  <main class="workspace">
    <h1 class="headline">Ready when you are.</h1>
    
    <!-- Next-Gen Prompt Pill -->
    <div class="input-pill">
      <button class="btn-add">+</button>
      <textarea placeholder="Ask anything or drop files here..."></textarea>

      <!-- Advanced Thinking Selector -->
      <div class="reasoning-slider" title="Select Thinking Depth">
        <span class="step active"></span>
        <span class="step"></span>
        <span class="step"></span>
      </div>

      <button class="btn-mic"></button>
      <button class="btn-voice-aura"></button>
    </div>
  </main>
</div>
```

```css
/* Unique Component Styles */
.input-pill {
  width: 100%;
  max-width: 720px;
  background: #212121;
  border: 1px solid #333333;
  border-radius: 9999px;
  padding: 10px 18px;
  display: flex;
  align-items: center;
  gap: 12px;
  transition: border-color 0.2s ease, box-shadow 0.2s ease;
}

.input-pill:focus-within {
  border-color: #3b82f6;
  box-shadow: 0 0 24px rgba(59, 130, 246, 0.2);
}

.reasoning-slider {
  display: flex;
  gap: 4px;
  background: #171717;
  padding: 4px 8px;
  border-radius: 12px;
  cursor: pointer;
}

.reasoning-slider .step {
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background: #444;
}

.reasoning-slider .step.active {
  background: #3b82f6;
  box-shadow: 0 0 6px #3b82f6;
}
``