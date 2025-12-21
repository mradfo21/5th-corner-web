# 🎨 R.A.S.T.E.R. Dashboard Design Guide

**FOR:** Game API Dashboard Development  
**PURPOSE:** Create a visually cohesive admin dashboard that matches the main website's aesthetic  
**THEME:** Recovered government material / Institutional VHS / SCP-inspired

---

## 🎯 Core Design Philosophy

### **NOT This:**
- ❌ Modern, sleek, colorful dashboards
- ❌ Gradients and drop shadows
- ❌ Playful or friendly UI
- ❌ High-tech cyberpunk neon
- ❌ Material Design or Bootstrap defaults

### **YES This:**
- ✅ **Recovered government documentation**
- ✅ **Cold, institutional, bureaucratic**
- ✅ **VHS tape degradation**
- ✅ **Classified archive material**
- ✅ **1990s military/research facility terminals**
- ✅ **Feels like evidence, not a product**

---

## 🎨 Color Palette (Exact Values)

### **Primary Colors**
```css
--color-blood-red: #dc143c;        /* Primary accent - buttons, borders, warnings */
--color-dark-red: #8b0000;         /* Hover states, darker accents */
--color-near-black: #0a0a0a;       /* Main background */
--color-dark-gray: #1a1a1a;        /* Secondary background, cards */
--color-off-white: #e0e0e0;        /* Primary text */
```

### **Supporting Colors**
```css
--color-text-dim: rgba(224, 224, 224, 0.7);      /* Secondary text */
--color-text-faint: rgba(224, 224, 224, 0.5);    /* Tertiary text, labels */
--color-text-ghost: rgba(224, 224, 224, 0.3);    /* Disabled, placeholders */

--color-border-red: rgba(220, 20, 60, 0.5);      /* Default borders */
--color-border-bright: rgba(220, 20, 60, 0.8);   /* Active borders */

--color-success: #4caf50;          /* Status: alive, success */
--color-warning: #ff9800;          /* Status: warning, attention */
--color-danger: #dc143c;           /* Status: dead, error */
```

### **Background Overlays**
```css
--overlay-dark: rgba(10, 10, 10, 0.9);
--overlay-medium: rgba(26, 26, 26, 0.8);
--overlay-light: rgba(50, 50, 50, 0.6);
```

---

## 📝 Typography

### **Font Stack**
```css
/* Monospace/OCR - For titles, labels, system text */
--font-ocr: 'Share Tech Mono', 'Courier Prime', 'Courier New', monospace;

/* Sans-serif - For body copy, longer text */
--font-din: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
```

**How to use:**
- **Headers, labels, system text:** OCR monospace
- **Body copy, descriptions, paragraphs:** DIN/Inter
- **Data tables, JSON, code:** OCR monospace

### **Font Sizes**
```css
--text-xs: 0.65rem;      /* Timestamps, metadata */
--text-sm: 0.75rem;      /* Labels, small text */
--text-base: 0.85rem;    /* Body copy */
--text-md: 1rem;         /* Section headers */
--text-lg: 1.2rem;       /* Page titles */
--text-xl: 1.5rem;       /* Major headings */
```

### **Letter Spacing**
```css
/* Monospace text should be WIDE */
letter-spacing: 0.2em;   /* Headers, labels */
letter-spacing: 0.1em;   /* Body monospace */
letter-spacing: 0.05em;  /* Sans-serif body */
```

### **Text Hierarchy Example**
```css
/* Page Title */
.page-title {
    font-family: var(--font-ocr);
    font-size: 1.5rem;
    letter-spacing: 0.3em;
    color: var(--color-blood-red);
    text-transform: uppercase;
    font-weight: normal;
}

/* Section Header */
.section-header {
    font-family: var(--font-ocr);
    font-size: 1rem;
    letter-spacing: 0.2em;
    color: var(--color-off-white);
    text-transform: uppercase;
    border-bottom: 1px solid var(--color-border-red);
    padding-bottom: 8px;
}

/* Body Text */
.body-text {
    font-family: var(--font-din);
    font-size: 0.85rem;
    letter-spacing: 0.05em;
    color: var(--color-text-dim);
    line-height: 1.6;
}

/* Label/Metadata */
.label {
    font-family: var(--font-ocr);
    font-size: 0.65rem;
    letter-spacing: 0.15em;
    color: var(--color-text-faint);
    text-transform: uppercase;
}
```

---

## 🎬 Essential Visual Effects

### **1. VHS Scanlines (REQUIRED)**

Add this to your `<body>` tag:

```css
body::before {
    content: '';
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: repeating-linear-gradient(
        0deg,
        rgba(0, 0, 0, 0.15),
        rgba(0, 0, 0, 0.15) 1px,
        transparent 1px,
        transparent 2px
    );
    pointer-events: none;
    z-index: 9999;
    animation: scanlines 8s linear infinite;
}

@keyframes scanlines {
    0% { transform: translateY(0); }
    100% { transform: translateY(10px); }
}
```

**Critical:** This MUST be on every page. It's the signature VHS effect.

---

### **2. Red Chromatic Aberration (Hover Effects)**

For interactive elements (buttons, cards, links):

```css
.interactive-element {
    position: relative;
    transition: all 0.3s ease;
}

.interactive-element:hover {
    text-shadow: 
        -2px 0 0 rgba(220, 20, 60, 0.5),
        2px 0 0 rgba(220, 20, 60, 0.3);
}

/* For elements with backgrounds */
.card:hover {
    box-shadow: 
        -3px 0 0 rgba(220, 20, 60, 0.3),
        3px 0 0 rgba(220, 20, 60, 0.2),
        0 0 20px rgba(220, 20, 60, 0.1);
    border-color: var(--color-blood-red);
}
```

**Rule:** ALWAYS use RED for hover effects, never green, blue, or cyan.

---

### **3. Glitch Effect (Optional, Use Sparingly)**

Only for critical titles or warnings:

```css
.glitch {
    position: relative;
}

.glitch::before,
.glitch::after {
    content: attr(data-text);
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
}

.glitch::before {
    color: rgba(220, 20, 60, 0.8);
    z-index: -1;
    animation: glitch-1 2s infinite;
}

.glitch::after {
    color: rgba(220, 20, 60, 0.5);
    z-index: -2;
    animation: glitch-2 3s infinite;
}

@keyframes glitch-1 {
    0%, 100% { transform: translate(0); }
    20% { transform: translate(-2px, 2px); }
    40% { transform: translate(-2px, -2px); }
    60% { transform: translate(2px, 2px); }
    80% { transform: translate(2px, -2px); }
}

@keyframes glitch-2 {
    0%, 100% { transform: translate(0); }
    25% { transform: translate(2px, -2px); }
    50% { transform: translate(-2px, 2px); }
    75% { transform: translate(2px, 2px); }
}
```

**Usage:**
```html
<h1 class="glitch" data-text="ERROR">ERROR</h1>
```

**When to use:**
- Major warnings
- Error states
- Critical status changes
- NOT on regular text

---

## 🧱 Component Design Guidelines

### **Buttons**

```css
.btn {
    font-family: var(--font-ocr);
    font-size: 0.75rem;
    letter-spacing: 0.15em;
    text-transform: uppercase;
    padding: 8px 16px;
    border: 1px solid var(--color-border-red);
    background: transparent;
    color: var(--color-off-white);
    cursor: pointer;
    transition: all 0.3s ease;
}

.btn:hover {
    background: rgba(220, 20, 60, 0.1);
    border-color: var(--color-blood-red);
    box-shadow: 0 0 10px rgba(220, 20, 60, 0.3);
    color: var(--color-blood-red);
}

.btn:active {
    transform: scale(0.98);
}

.btn-primary {
    background: var(--color-blood-red);
    border-color: var(--color-blood-red);
    color: var(--color-near-black);
}

.btn-primary:hover {
    background: var(--color-dark-red);
    box-shadow: 0 0 15px rgba(220, 20, 60, 0.5);
}
```

**Button variants:**
- `.btn` - Default (outline)
- `.btn-primary` - Filled red
- `.btn-danger` - Critical actions (same as primary)
- `.btn-ghost` - Very subtle, low opacity

---

### **Cards / Panels**

```css
.card {
    background: var(--color-dark-gray);
    border: 1px solid rgba(220, 20, 60, 0.3);
    padding: 20px;
    margin-bottom: 20px;
    transition: all 0.3s ease;
}

.card:hover {
    border-color: var(--color-border-red);
    box-shadow: 0 0 15px rgba(220, 20, 60, 0.15);
}

.card-header {
    font-family: var(--font-ocr);
    font-size: 0.85rem;
    letter-spacing: 0.2em;
    text-transform: uppercase;
    color: var(--color-blood-red);
    margin-bottom: 12px;
    padding-bottom: 8px;
    border-bottom: 1px solid rgba(220, 20, 60, 0.3);
}

.card-body {
    font-family: var(--font-din);
    font-size: 0.85rem;
    color: var(--color-text-dim);
    line-height: 1.6;
}

.card-footer {
    margin-top: 12px;
    padding-top: 12px;
    border-top: 1px solid rgba(220, 20, 60, 0.2);
    font-size: 0.65rem;
    color: var(--color-text-faint);
}
```

---

### **Data Tables**

```css
.data-table {
    width: 100%;
    border-collapse: collapse;
    font-family: var(--font-ocr);
    font-size: 0.75rem;
}

.data-table thead {
    background: rgba(220, 20, 60, 0.1);
    border-bottom: 2px solid var(--color-blood-red);
}

.data-table th {
    padding: 12px 16px;
    text-align: left;
    font-weight: normal;
    letter-spacing: 0.15em;
    text-transform: uppercase;
    color: var(--color-blood-red);
}

.data-table td {
    padding: 10px 16px;
    border-bottom: 1px solid rgba(220, 20, 60, 0.2);
    color: var(--color-text-dim);
}

.data-table tbody tr {
    transition: background 0.2s ease;
}

.data-table tbody tr:hover {
    background: rgba(220, 20, 60, 0.05);
    cursor: pointer;
}

/* Alternating rows (optional) */
.data-table tbody tr:nth-child(even) {
    background: rgba(0, 0, 0, 0.2);
}
```

---

### **Status Indicators**

```css
.status {
    display: inline-block;
    padding: 4px 12px;
    font-family: var(--font-ocr);
    font-size: 0.65rem;
    letter-spacing: 0.15em;
    text-transform: uppercase;
    border-radius: 2px;
    border: 1px solid;
}

.status-alive {
    color: var(--color-success);
    border-color: var(--color-success);
    background: rgba(76, 175, 80, 0.1);
}

.status-dead {
    color: var(--color-danger);
    border-color: var(--color-danger);
    background: rgba(220, 20, 60, 0.1);
}

.status-active {
    color: var(--color-blood-red);
    border-color: var(--color-blood-red);
    background: rgba(220, 20, 60, 0.05);
    animation: pulse 2s ease-in-out infinite;
}

@keyframes pulse {
    0%, 100% { opacity: 1; }
    50% { opacity: 0.6; }
}
```

---

### **Loading States**

```css
.loading {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 16px;
    padding: 40px;
}

.loading-text {
    font-family: var(--font-ocr);
    font-size: 0.85rem;
    letter-spacing: 0.2em;
    color: var(--color-blood-red);
    text-transform: uppercase;
    animation: pulse 2s ease-in-out infinite;
}

.loading-dots {
    display: flex;
    gap: 8px;
}

.loading-dot {
    width: 8px;
    height: 8px;
    background: var(--color-blood-red);
    border-radius: 50%;
    animation: dotPulse 1.5s ease-in-out infinite;
}

.loading-dot:nth-child(2) { animation-delay: 0.2s; }
.loading-dot:nth-child(3) { animation-delay: 0.4s; }

@keyframes dotPulse {
    0%, 100% { transform: scale(1); opacity: 1; }
    50% { transform: scale(1.5); opacity: 0.5; }
}
```

---

### **Forms & Inputs**

```css
.form-group {
    margin-bottom: 20px;
}

.form-label {
    display: block;
    font-family: var(--font-ocr);
    font-size: 0.65rem;
    letter-spacing: 0.15em;
    text-transform: uppercase;
    color: var(--color-text-faint);
    margin-bottom: 6px;
}

.form-input {
    width: 100%;
    padding: 10px 12px;
    font-family: var(--font-ocr);
    font-size: 0.85rem;
    background: var(--color-near-black);
    border: 1px solid var(--color-border-red);
    color: var(--color-off-white);
    outline: none;
    transition: all 0.3s ease;
}

.form-input:focus {
    border-color: var(--color-blood-red);
    box-shadow: 0 0 10px rgba(220, 20, 60, 0.2);
}

.form-input::placeholder {
    color: var(--color-text-ghost);
    opacity: 1;
}

/* Textarea */
textarea.form-input {
    resize: vertical;
    min-height: 120px;
    font-family: var(--font-ocr);
}

/* Select dropdown */
select.form-input {
    cursor: pointer;
    background-image: url('data:image/svg+xml;utf8,<svg fill="%23dc143c" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16"><path d="M8 11L3 6h10z"/></svg>');
    background-repeat: no-repeat;
    background-position: right 10px center;
    background-size: 12px;
    padding-right: 35px;
}
```

---

## 📐 Layout Guidelines

### **Spacing System**
```css
--spacing-xs: 4px;
--spacing-sm: 8px;
--spacing-md: 16px;
--spacing-lg: 24px;
--spacing-xl: 40px;
--spacing-2xl: 60px;
```

### **Container Widths**
```css
.container {
    max-width: 1400px;
    margin: 0 auto;
    padding: 0 var(--spacing-lg);
}

.container-narrow {
    max-width: 900px;
}

.container-wide {
    max-width: 1800px;
}
```

### **Grid System**
```css
.grid {
    display: grid;
    gap: var(--spacing-lg);
}

.grid-2 { grid-template-columns: repeat(2, 1fr); }
.grid-3 { grid-template-columns: repeat(3, 1fr); }
.grid-4 { grid-template-columns: repeat(4, 1fr); }

/* Responsive */
@media (max-width: 1024px) {
    .grid-4 { grid-template-columns: repeat(2, 1fr); }
}

@media (max-width: 768px) {
    .grid-2, .grid-3, .grid-4 { 
        grid-template-columns: 1fr; 
    }
}
```

---

## 🎯 Dashboard-Specific Components

### **Session Card**

```css
.session-card {
    background: var(--color-dark-gray);
    border: 1px solid rgba(220, 20, 60, 0.3);
    padding: 20px;
    cursor: pointer;
    transition: all 0.3s ease;
}

.session-card:hover {
    border-color: var(--color-blood-red);
    box-shadow: 0 0 20px rgba(220, 20, 60, 0.2);
    transform: translateY(-2px);
}

.session-id {
    font-family: var(--font-ocr);
    font-size: 0.75rem;
    color: var(--color-blood-red);
    margin-bottom: 8px;
    letter-spacing: 0.1em;
}

.session-meta {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-top: 12px;
    padding-top: 12px;
    border-top: 1px solid rgba(220, 20, 60, 0.2);
}

.session-stat {
    font-family: var(--font-ocr);
    font-size: 0.65rem;
    color: var(--color-text-faint);
}

.session-stat strong {
    color: var(--color-off-white);
    margin-left: 4px;
}
```

---

### **History Timeline**

```css
.timeline {
    position: relative;
    padding-left: 40px;
}

.timeline::before {
    content: '';
    position: absolute;
    left: 12px;
    top: 0;
    bottom: 0;
    width: 2px;
    background: linear-gradient(
        to bottom,
        var(--color-blood-red),
        rgba(220, 20, 60, 0.3)
    );
}

.timeline-item {
    position: relative;
    margin-bottom: 24px;
    padding-left: 20px;
}

.timeline-item::before {
    content: '';
    position: absolute;
    left: -28px;
    top: 6px;
    width: 8px;
    height: 8px;
    background: var(--color-blood-red);
    border: 2px solid var(--color-near-black);
    border-radius: 50%;
}

.timeline-turn {
    font-family: var(--font-ocr);
    font-size: 0.65rem;
    color: var(--color-text-faint);
    text-transform: uppercase;
    margin-bottom: 4px;
}

.timeline-action {
    font-family: var(--font-din);
    font-size: 0.85rem;
    color: var(--color-text-dim);
}
```

---

### **JSON/Code Display**

```css
.code-block {
    background: var(--color-near-black);
    border: 1px solid rgba(220, 20, 60, 0.3);
    border-left: 3px solid var(--color-blood-red);
    padding: 16px;
    overflow-x: auto;
    font-family: var(--font-ocr);
    font-size: 0.75rem;
    line-height: 1.6;
}

.code-block pre {
    margin: 0;
    color: var(--color-text-dim);
}

/* Syntax highlighting */
.json-key { color: var(--color-blood-red); }
.json-string { color: var(--color-text-dim); }
.json-number { color: #4caf50; }
.json-boolean { color: #ff9800; }
.json-null { color: var(--color-text-ghost); }
```

---

## 📱 Responsive Design

### **Breakpoints**
```css
/* Mobile: < 600px */
/* Tablet: 600px - 1024px */
/* Desktop: > 1024px */

@media (max-width: 600px) {
    :root {
        --text-xs: 0.6rem;
        --text-sm: 0.7rem;
        --text-base: 0.8rem;
        --spacing-md: 12px;
        --spacing-lg: 16px;
    }
    
    .card {
        padding: 16px;
    }
    
    .data-table {
        font-size: 0.65rem;
    }
    
    .data-table th,
    .data-table td {
        padding: 8px 10px;
    }
}
```

---

## ⚠️ Critical Dos and Don'ts

### **DO:**
- ✅ Use monospace fonts for all system text
- ✅ Use RED as the only accent color
- ✅ Add scanlines overlay to every page
- ✅ Use uppercase for labels and headers
- ✅ Add generous letter-spacing to monospace text
- ✅ Use dark backgrounds (near-black)
- ✅ Make interactive elements subtle until hover
- ✅ Add transitions (0.3s ease)
- ✅ Use borders, not drop shadows (except red glows)
- ✅ Keep animations slow and deliberate

### **DON'T:**
- ❌ Use bright colors (blue, cyan, green accents)
- ❌ Use rounded corners (except 2-3px max)
- ❌ Use gradients or complex patterns
- ❌ Use comic fonts or handwriting fonts
- ❌ Make things "bouncy" or playful
- ❌ Use emoji (except sparingly in documentation)
- ❌ Add confetti or celebration animations
- ❌ Use stock photography
- ❌ Make hover effects green or blue
- ❌ Use white backgrounds

---

## 🖼️ Example Full Page Layout

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>R.A.S.T.E.R. Operations</title>
    <style>
        /* Include all CSS from above */
    </style>
</head>
<body>
    <!-- Header -->
    <header class="header">
        <div class="container">
            <h1 class="header-title">R.A.S.T.E.R. OPERATIONS</h1>
            <nav class="header-nav">
                <a href="/sessions">Sessions</a>
                <a href="/history">History</a>
                <a href="/tapes">VHS Tapes</a>
            </nav>
        </div>
    </header>

    <!-- Main Content -->
    <main class="main">
        <div class="container">
            <!-- Page Title -->
            <div class="page-header">
                <h1 class="page-title">Active Sessions</h1>
                <button class="btn btn-primary">+ New Session</button>
            </div>

            <!-- Session Grid -->
            <div class="grid grid-3">
                <div class="session-card">
                    <div class="session-id">SESSION-001</div>
                    <div class="status status-alive">ALIVE</div>
                    <div class="session-meta">
                        <span class="session-stat">Turn: <strong>12</strong></span>
                        <span class="session-stat">Location: <strong>Hallway</strong></span>
                    </div>
                </div>
                <!-- More cards... -->
            </div>
        </div>
    </main>

    <!-- Footer -->
    <footer class="footer">
        <div class="container">
            <p class="footer-text">R.A.S.T.E.R. © 2025</p>
        </div>
    </footer>
</body>
</html>
```

---

## 🔗 Reference Implementation

Your main website already implements this aesthetic perfectly. For reference:

**Main Website URL:** `https://fiveth-corner-operations.onrender.com`

**Key pages to study:**
- `/` - Landing page (hero, typography, colors)
- `/admin` - The wrapper page you'll be embedded in
- `/404` - Error page styling

**Files to reference:**
- `static/css/style.css` - Complete stylesheet
- `templates/admin.html` - Dashboard wrapper design
- `templates/index.html` - Component examples

---

## 🎯 Dashboard-Specific Requirements

### **Your dashboard MUST have:**

1. **Scanlines overlay** - Signature VHS effect
2. **Red accent color only** - No cyan, blue, or green
3. **OCR-B/monospace typography** - For all system text
4. **Dark near-black background** - `#0a0a0a`
5. **Uppercase labels** - With letter-spacing
6. **Red chromatic aberration hovers** - On all interactive elements
7. **Institutional feel** - Cold, bureaucratic, not friendly
8. **Responsive design** - Mobile-friendly tables and grids

### **Nice to have:**
- Auto-refresh indicator
- Glitch effect on critical warnings
- Subtle animation on status changes
- Toast notifications (red themed)
- Keyboard shortcuts (easter eggs)

---

## 📊 Performance Guidelines

### **Keep It Fast:**
- Minimize CSS animations (only scanlines, hover effects)
- Use CSS transforms over position changes
- Lazy load images/GIFs
- Debounce auto-refresh (5-10 seconds minimum)
- Use `will-change` sparingly

### **Accessibility:**
- All interactive elements must be keyboard accessible
- Status indicators should have aria-labels
- Red/green color combos should also have text labels
- Font size minimum: 0.65rem (readable on mobile)

---

## 🧪 Testing Checklist

Before considering the dashboard complete:

- [ ] Scanlines visible on all pages
- [ ] All text uses OCR or DIN fonts
- [ ] All hovers use RED chromatic aberration
- [ ] No bright colors (blue, cyan, green) anywhere
- [ ] All labels are uppercase with letter-spacing
- [ ] Background is near-black (`#0a0a0a`)
- [ ] Buttons match the style guide
- [ ] Cards/panels have red borders
- [ ] Tables use monospace font
- [ ] Status indicators have correct colors
- [ ] Loading states match design
- [ ] Responsive on mobile (< 600px)
- [ ] No drop shadows (except red glows)
- [ ] Transitions are 0.3s ease
- [ ] Forms match input styling

---

## 🚀 Quick Start Template

Here's a minimal starter template:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>R.A.S.T.E.R. Admin</title>
    
    <!-- Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Courier+Prime:wght@400;700&family=Share+Tech+Mono&family=Inter:wght@300;400;600&display=swap" rel="stylesheet">
    
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        
        :root {
            --color-blood-red: #dc143c;
            --color-near-black: #0a0a0a;
            --color-dark-gray: #1a1a1a;
            --color-off-white: #e0e0e0;
            --font-ocr: 'Share Tech Mono', 'Courier Prime', monospace;
            --font-din: 'Inter', sans-serif;
        }
        
        body {
            background: var(--color-near-black);
            color: var(--color-off-white);
            font-family: var(--font-din);
            min-height: 100vh;
        }
        
        /* VHS SCANLINES - REQUIRED */
        body::before {
            content: '';
            position: fixed;
            top: 0; left: 0;
            width: 100%; height: 100%;
            background: repeating-linear-gradient(
                0deg,
                rgba(0, 0, 0, 0.15), rgba(0, 0, 0, 0.15) 1px,
                transparent 1px, transparent 2px
            );
            pointer-events: none;
            z-index: 9999;
            animation: scanlines 8s linear infinite;
        }
        
        @keyframes scanlines {
            0% { transform: translateY(0); }
            100% { transform: translateY(10px); }
        }
        
        /* YOUR STYLES HERE */
    </style>
</head>
<body>
    <div class="container">
        <h1 class="page-title">R.A.S.T.E.R.</h1>
        <!-- Your dashboard content -->
    </div>
</body>
</html>
```

---

## 📞 Questions?

If you're unsure about a design decision, ask yourself:

**"Does this look like recovered government documentation from 1993, or does it look like a modern web app?"**

If it's the latter, dial it back. Less is more. Cold, institutional, bureaucratic.

---

## ✅ Final Checklist

Your dashboard is ready when:

- [x] Looks like it could be from a 1990s government facility
- [x] Feels cold, not friendly
- [x] Uses only red accents (no other colors)
- [x] Has VHS scanlines overlay
- [x] Uses OCR-B/monospace typography
- [x] All interactive elements have red hover effects
- [x] No drop shadows (except red glows)
- [x] Dark near-black background throughout
- [x] Could be mistaken for SCP Foundation archives
- [x] Makes you feel like you're looking at classified material

---

**Good luck building the dashboard!** 🎮📼

**Remember:** You're not building a product UI. You're designing **evidence**.

---

**Last Updated:** 2025-12-20  
**Version:** 1.0  
**Theme:** Institutional VHS / Recovered Government Material

