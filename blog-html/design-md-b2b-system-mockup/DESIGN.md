# B2B Admin Console Design System

## Visual Theme & Atmosphere
- Impression: Reliable, auditable, operational clarity
- Tone: Calm, enterprise, high information density without visual noise
- Metaphor: "Control tower for operations"
- Avoid: Consumer-style playful gradients, oversized hero banners, decorative illustrations

## Color Palette & Roles
- Primary: `#1F4B99` - top nav active state, primary CTAs
- Secondary: `#0E9F6E` - healthy status, success actions
- Critical: `#D92D20` - incidents, destructive actions
- Warning: `#F79009` - risk alerts, pending approvals
- Info: `#2563EB` - contextual links, neutral callouts
- Text Primary: `#111827`
- Text Secondary: `#4B5563`
- Surface: `#FFFFFF`
- Surface Subtle: `#F9FAFB`
- Border: `#E5E7EB`
- Focus Ring: `#93C5FD`

## Typography
- Font stack: `"Inter", "Noto Sans", "Segoe UI", sans-serif`
- H1: 30px / 700 / 1.25
- H2: 24px / 700 / 1.3
- H3: 18px / 600 / 1.4
- Body: 14px / 400 / 1.6
- Small: 12px / 400 / 1.5
- Data number (KPI): 28px / 700 / 1.2

## Spacing & Sizing
- Base unit: 8px
- Page padding: 24px desktop, 16px tablet/mobile
- Grid gap: 16px
- Card padding: 16px
- Section gap: 24px
- Button height: 36px
- Input height: 36px
- Table row height: 44px

## Components

### Top Navigation
- Height: 56px
- Left: product + environment badge (Production / Staging)
- Center: global search
- Right: notifications, user menu

### Side Navigation
- Width: 240px (collapsed 72px)
- Grouped by domain: Overview, Operations, Users, Integrations, Billing, Audit
- Active item: primary background tint + left 3px accent

### KPI Card
- Includes title, value, trend, period
- Trend states: up (secondary), down (critical), flat (text secondary)
- Optional mini sparkline

### Data Table
- Sticky header
- Sortable columns
- Row selection checkbox
- Inline status badge + action menu per row

### Status Badge
- Success: secondary tint
- Warning: warning tint
- Error: critical tint
- Info: info tint
- Must include text label, not color-only meaning

### Action Area
- Primary action appears once per view
- Secondary actions in overflow menu
- Destructive actions require confirmation modal with resource name

## Layout Principles
- Max content width: 1440px
- Desktop layout: top nav + side nav + content area
- Main dashboard above the fold:
  1. System health banner
  2. KPI row (4-6 cards)
  3. Incident table + queue panel
- Detail screens:
  - Header with title and key actions
  - Filters and saved views
  - Table/list body
  - Right drawer for details

## Content & Interaction Rules
- One screen = one operational objective
- Prioritize anomaly visibility over decorative balance
- Every critical metric must show timestamp + source
- Empty state must provide next action
- Error state must provide recovery action
- Keyboard accessible for all core actions

## Responsive Behavior
- >=1280px: full side nav + 2-column detail layout
- 768-1279px: collapsible side nav + single content column
- <768px: focus on queue triage and approvals only, hide low-priority widgets

## Accessibility
- Minimum contrast ratio: 4.5:1 for text
- Visible focus states on all interactive controls
- Tables support screen-reader headers
- Status communicated by text and icon, not color only
