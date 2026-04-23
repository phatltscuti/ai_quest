```markdown
# Design System Specification: Enterprise Precision & Tonal Depth

## 1. Overview & Creative North Star
### The Creative North Star: "The Architectural Ledger"
In the world of high-density compliance and system management, clarity is not just a feature—it is a requirement. This design system rejects the "bubbly" aesthetics of consumer SaaS in favor of **Architectural Ledgering**. 

The system is built on the principle of **Inherent Order**. We achieve professional authority not through heavy borders or decorative flair, but through a rigorous adherence to typographic hierarchy and tonal layering. The interface should feel like a high-end, precision-engineered instrument: silent, powerful, and impeccably organized. We break the "template" look by using wide-format horizontal layouts and asymmetric data densities that guide the eye to critical system statuses without visual noise.

---

## 2. Colors: The Tonal Spectrum
Our palette is a sophisticated range of deep cold blues and architectural grays. This is a functional palette where color is used strictly as information.

### The "No-Line" Rule
**Explicit Instruction:** Designers are prohibited from using 1px solid borders to define sections. 
*   **How to define boundaries:** Use background shifts. A `surface-container-low` (#f1f3ff) section sitting on a `surface` (#f9f9ff) background provides enough contrast for the eye to perceive a boundary without the visual stutter of a line.

### Surface Hierarchy & Nesting
Treat the UI as a physical stack of technical documents.
*   **Base:** `surface` (#f9f9ff)
*   **Sub-Section:** `surface-container-low` (#f1f3ff)
*   **Active Content Area:** `surface-container-lowest` (#ffffff)
*   **Elevated Overlays:** `surface-container-highest` (#d8e2ff)

### The "Glass & Gradient" Rule
For high-level system dashboards, use **Glassmorphism** to keep the user oriented. Floating utility panels should use `surface` at 80% opacity with a `backdrop-blur` of 20px. 
*   **Signature Texture:** Use a subtle linear gradient for primary actions: `primary` (#27609d) to `primary_dim` (#145490) at a 135-degree angle. This adds a "machined" metallic depth that flat fills lack.

---

## 3. Typography: The Information Hierarchy
We utilize **Inter** across the entire system. Its neutral, high-x-height construction is perfect for the legibility required in compliance monitoring.

*   **Display (lg/md/sm):** Used exclusively for high-level system health scores or aggregate data points.
*   **Headline (lg/md/sm):** Reserved for primary module titles. Use `on_surface` (#143161) with `font-weight: 600` to establish authority.
*   **Title (lg/md/sm):** Used for data group headers. These should feel "pinned" to their sections.
*   **Body (lg/md/sm):** The workhorse. All system logs and compliance descriptions must use `body-md` (0.875rem) for the optimal balance of density and readability.
*   **Label (md/sm):** Used for table headers and micro-metadata. 

**The Editorial Shift:** Increase the `letter-spacing` of `label-sm` by 0.05rem and set to uppercase for a "technical spec" feel when labeling hardware or status IDs.

---

## 4. Elevation & Depth: Tonal Layering
Traditional shadows are often too "soft" for an enterprise environment. We use **Tonal Layering** to define the Z-axis.

### The Layering Principle
Depth is achieved by "stacking." 
1.  **Level 0 (Background):** `surface`
2.  **Level 1 (Cards/Tables):** `surface-container-lowest`
3.  **Level 2 (Active States):** `surface-container-high`

### Ambient Shadows
If a floating element (like a modal) is required, use an **Ambient Shadow**:
*   `box-shadow: 0 12px 40px rgba(20, 49, 97, 0.08);` 
*   Note the use of the `on_surface` color (#143161) as the shadow tint rather than pure black. This makes the shadow feel like a natural occlusion of light.

### The "Ghost Border" Fallback
Where accessibility requirements demand a container boundary, use a **Ghost Border**: `outline-variant` (#99b2e9) at **15% opacity**. It should be felt, not seen.

---

## 5. Components: Functional Primitives

### Buttons
*   **Primary:** Gradient fill (`primary` to `primary_dim`), `radius-md` (0.375rem). No border.
*   **Secondary:** `surface-container-high` fill with `on_primary_fixed_variant` text.
*   **States:** Hover should trigger a 10% brightness increase; Pressed should trigger a 5% brightness decrease.

### Input Fields
*   **Structure:** No background fill. Use a `Ghost Border` bottom-line only for a sophisticated "form" look, or a full `outline` (#617aae) at 20% opacity for high-density data entry.
*   **Focus State:** Shift border to `primary` (#27609d) with a 2px thickness.

### Cards & Data Lists
*   **Constraint:** Forbid the use of horizontal divider lines between list items.
*   **Solution:** Use a 0.2rem (`space-1`) vertical gap and alternating background tints (`surface` vs `surface-container-low`) for row striped effects.

### Status Indicators (High-Density)
*   **Critical:** `error` (#9f403d) - Use for system failures.
*   **Warning:** `on_secondary_container` (#465365) - Use for non-critical compliance drifts.
*   **Healthy:** `tertiary` (#006e3a) - Use for "In Compliance" states.
*   *Styling Note:* Use a 6px solid circle (Dot) next to the text label rather than a large badge to maintain high data density.

---

## 6. Do's and Don'ts

### Do
*   **Do** use `spacing-4` (0.9rem) as your standard gutter between data columns.
*   **Do** align all text to a 4px baseline grid to ensure vertical rhythm.
*   **Do** use `surface-variant` to de-emphasize secondary information like "Last Updated" timestamps.
*   **Do** leverage `surface-container-highest` for "Hover" states on interactive table rows.

### Don't
*   **Don't** use pure black (#000000) for text. Use `on_surface` (#143161) to maintain the deep-blue professional tone.
*   **Don't** use rounded corners larger than `xl` (0.75rem). The system should feel structural and precise, not "friendly."
*   **Don't** use icons without text labels in primary navigation. Compliance requires zero ambiguity.
*   **Don't** use "Drop Shadows" on standard cards. Stick to Tonal Layering.

---

## 7. Spacing & Grid Logic
The system relies on a **Compact Fluid Grid**. 
*   **Density:** Use `spacing-2.5` (0.5rem) for internal component padding (e.g., inside a button or input).
*   **Sectioning:** Use `spacing-10` (2.25rem) to separate major functional blocks.
*   **Data Groups:** Use `spacing-5` (1.1rem) to group related form fields or data points.

By adhering to these constraints, you will create an interface that feels like a singular, integrated piece of high-performance software rather than a collection of disparate widgets.