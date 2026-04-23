# Phat Dev Intro - Automated Video with Antigravity + Remotion

A personal introduction video created **entirely by AI** using Google Antigravity IDE + Remotion framework.

## Demo

| Demo Tutorial | Result Video |
|---|---|
| [![Demo](https://img.shields.io/badge/YouTube-Demo_Tutorial-red?logo=youtube)](https://www.youtube.com/watch?v=YOUR_DEMO_VIDEO_ID) | [![Result](https://img.shields.io/badge/YouTube-Result_Video-red?logo=youtube)](https://www.youtube.com/watch?v=YOUR_RESULT_VIDEO_ID) |

## About

This project was generated using the workflow:

1. **Antigravity IDE** receives a natural language prompt describing the video
2. The AI agent (with `remotion-best-practices` skill) writes React/TypeScript code
3. **Remotion** renders the code into an MP4 video

No manual video editing was involved.

## Profile in Video

- **Name:** Ly Tan Phat
- **Role:** PHP Developer
- **Company:** Scuti
- **Skills:** PHP, Laravel, MySQL, REST API, Docker, Git
- **Tagline:** "Building scalable web solutions with PHP, Laravel & modern tech"

## Video Scenes

| Scene | Time | Description |
|---|---|---|
| 1 - Avatar Reveal | 0-5s | Dark blue background, avatar fades in with glow effect, name appears with typewriter animation |
| 2 - Role & Skills | 5-12s | "PHP Developer @ Scuti", skill badges animate in one by one |
| 3 - Tagline | 12-18s | Tagline reveals with elegant motion, code-rain background effect |
| 4 - Call to Action | 18-20s | "Let's connect!" with GitHub/LinkedIn icons, smooth fade out |

## Tech Stack

- [Remotion](https://remotion.dev) - React framework for programmatic video creation
- [Google Antigravity](https://antigravity.google) - AI-powered IDE
- React + TypeScript
- TailwindCSS

## Getting Started

### Prerequisites

- Node.js (LTS version)
- npm or yarn

### Installation

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO.git
cd YOUR_REPO
npm install
```

### Development

```bash
npm run dev
```

Open [http://localhost:3000](http://localhost:3000) and select the `PhatDevIntro` composition to preview.

### Render MP4

```bash
npx remotion render PhatDevIntro out/phat-dev-intro.mp4
```

The output file will be at `out/phat-dev-intro.mp4`.

## Project Structure

```
my-video/
├── public/
│   └── logo.png              # Avatar / logo image
├── src/
│   ├── PhatDevIntro/
│   │   ├── Scene1-AvatarReveal.tsx
│   │   ├── Scene2-RoleSkills.tsx
│   │   ├── Scene3-Tagline.tsx
│   │   └── Scene4-CallToAction.tsx
│   ├── Root.tsx
│   └── index.ts
├── package.json
└── remotion.config.ts
```

## How It Was Made

Full blog post (Vietnamese + English):
- [Blog Vietnamese](https://YOUR_BLOG_URL/antigravity-remotion-video-blog.html)
- [Blog English](https://YOUR_BLOG_URL/antigravity-remotion-video-blog-en.html)

Reference video: [AntiGravity's New VIDEO Editing (Remotion) Skills Are Insane](https://www.youtube.com/watch?v=l5L3iZzk408) by Surya

## License

MIT

## Author

**Ly Tan Phat** - PHP Developer @ Scuti

- GitHub: [@YOUR_USERNAME](https://github.com/YOUR_USERNAME)
- LinkedIn: [YOUR_LINKEDIN](https://linkedin.com/in/YOUR_LINKEDIN)
