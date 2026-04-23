# EduNova AI Product Strategy 2026

**Document Classification:** Internal — Board & Leadership Only
**Version:** 2.0 | **Date:** January 15, 2026
**Author:** Dr. Minh Tran (CTO), Sarah Chen (VP of AI)

---

## Executive Summary

EduNova's 2026 product strategy centers on three AI pillars that will transform how students learn, teachers create, and institutions make decisions. We are investing $12.8M (45% of projected operating budget) in R&D, with 75 AI/ML engineers by end of year.

**Vision:** Every learner in Southeast Asia has access to a world-class AI tutor that adapts to their unique learning style, pace, and goals.

---

## Pillar 1: AI-Powered Personalized Tutoring

### Current State (End of 2025)
- AI Tutor available for Math and Science only
- 85,000 active users in beta
- Average 23% improvement in test scores
- Response latency: ~3.2 seconds

### 2026 Roadmap

**Q1 2026: Full Subject Expansion**
- Expand AI Tutor to cover English Language, History, Geography, and Biology
- Train specialized LLM models for each subject using EduNova's proprietary curriculum dataset (50,000+ lesson plans)
- Target: 300,000 active AI Tutor users by end of Q1

**Q2 2026: Adaptive Learning Engine v2**
- Real-time difficulty adjustment based on student performance patterns
- Multi-modal support: text, voice, image (students can photograph a math problem)
- Integration with school exam calendars for targeted revision
- Target: reduce response latency to <1.5 seconds

**Q3 2026: Group Study & Peer Learning**
- AI-facilitated study groups (3-5 students matched by level and learning style)
- Collaborative problem-solving with AI moderator
- Teacher dashboard to monitor group progress
- Target: 50,000 active study groups

**Q4 2026: Philippines Launch**
- Localize AI Tutor for Filipino K-12 curriculum
- Partnership with DepEd (Department of Education Philippines)
- Local content team: 15 curriculum specialists
- Target: 200,000 users in Philippines by end of Q4

### Key Metrics & Targets

| Metric | 2025 Actual | 2026 Target |
|--------|-------------|-------------|
| AI Tutor Active Users | 85,000 | 800,000 |
| Subjects Covered | 2 | 8 |
| Avg. Test Score Improvement | 23% | 30% |
| Response Latency | 3.2s | <1.5s |
| Student Satisfaction (CSAT) | 4.2/5 | 4.6/5 |

---

## Pillar 2: Generative Content Creation for Teachers

### Current State (End of 2025)
- Content Creator Studio launched in Q2 2025
- 2,400 teachers onboarded
- Reduces course creation time by 80% (40h → 8h)
- Generates: lesson plans, quizzes, worksheets, presentations

### 2026 Roadmap

**Q1 2026: Video Lesson Generator**
- AI generates animated video lessons from teacher's lesson plan text
- Support for Vietnamese, Thai, Indonesian, English voiceover
- Integrated with EduNova's illustration library (10,000+ educational graphics)
- Target: 500 video lessons generated per month

**Q2 2026: Curriculum Alignment Engine**
- Automatic alignment with national curriculum standards (Vietnam, Thailand, Indonesia)
- Gap analysis: identifies topics not yet covered in teacher's course
- Suggests supplementary content from EduNova's library
- Target: 90% of generated content meets curriculum standards

**Q3 2026: Assessment Generator Pro**
- AI creates differentiated assessments (easy/medium/hard) from a single topic
- Bloom's Taxonomy tagging for each question
- Anti-cheating: generates unique question variants per student
- Target: 100,000 assessments generated per month

**Q4 2026: Teacher Marketplace**
- Platform for teachers to share and sell AI-generated courses
- Revenue share: 70% teacher / 30% EduNova
- Quality review system powered by AI + peer review
- Target: 500 courses listed, $200K GMV in first quarter

### Key Metrics & Targets

| Metric | 2025 Actual | 2026 Target |
|--------|-------------|-------------|
| Active Teacher Users | 2,400 | 12,000 |
| Courses Created | 8,500 | 45,000 |
| Avg. Creation Time | 8 hours | 4 hours |
| Content Quality Score | 3.8/5 | 4.4/5 |
| Video Lessons Generated | 0 | 6,000/year |

---

## Pillar 3: Predictive Learning Analytics

### Current State (End of 2025)
- Learning Analytics Dashboard deployed to 120 schools
- Early warning system: 92% accuracy in identifying at-risk students
- Reports: student progress, class performance, curriculum coverage

### 2026 Roadmap

**Q1 2026: Institutional Analytics Suite**
- School-level and district-level aggregated dashboards
- Benchmark comparisons (school vs. national average)
- Exportable reports for ministry/accreditation compliance
- Target: 300 schools using institutional analytics

**Q2 2026: Predictive Dropout Prevention**
- ML model predicting dropout risk 8 weeks in advance (target: 95% accuracy)
- Automated intervention workflows: notify teacher, suggest remediation, alert parents
- Integration with student counseling systems
- Target: prevent 2,000+ potential dropouts

**Q3 2026: Learning Outcome Optimization**
- AI recommends optimal learning paths based on historical performance data
- A/B testing framework for teaching methodologies
- ROI calculator for schools: investment in EduNova vs. student outcome improvement
- Target: demonstrate 35% improvement in standardized test scores for active users

**Q4 2026: Enterprise Analytics**
- Custom analytics for corporate training clients
- Skill gap analysis: map employee skills to company's competency framework
- Training ROI dashboard: link learning completion to performance metrics
- Target: 30 enterprise clients using analytics module

### Key Metrics & Targets

| Metric | 2025 Actual | 2026 Target |
|--------|-------------|-------------|
| Schools Using Analytics | 120 | 400 |
| At-Risk Student Detection Accuracy | 92% | 95% |
| Dropout Prevention (students saved) | N/A | 2,000+ |
| Enterprise Analytics Clients | 0 | 30 |
| Data Points Processed/Day | 5M | 25M |

---

## Technology Infrastructure

### AI/ML Stack
- **Foundation Models:** Fine-tuned Gemini Pro for tutoring, PaLM 2 for content generation
- **Custom Models:** Proprietary student behavior prediction model (trained on 500M+ learning events)
- **Infrastructure:** Google Cloud Platform (GCP), Vertex AI for model training/serving
- **Edge Computing:** On-device inference for offline mobile tutoring (TensorFlow Lite)

### Data & Privacy
- All student data encrypted at rest (AES-256) and in transit (TLS 1.3)
- PDPD (Vietnam) and PDPA (Thailand) compliant
- Data residency: Vietnam data stays in GCP asia-southeast1 (Singapore)
- Annual third-party security audit (SOC 2 Type II certification in progress)

---

## Budget Allocation 2026

| Category | Budget | % of Total |
|----------|--------|-----------|
| AI/ML R&D (models, training, compute) | $5.8M | 45% |
| Product Engineering (platform, mobile) | $3.2M | 25% |
| Sales & Marketing | $2.6M | 20% |
| Operations & Infrastructure | $1.2M | 10% |
| **Total** | **$12.8M** | **100%** |

---

## Risk Factors

1. **Model Quality:** AI-generated content may contain errors; implementing human-in-the-loop review for all published content
2. **Compute Costs:** LLM inference costs could exceed budget if usage scales faster than projected; negotiating volume discounts with GCP
3. **Teacher Adoption:** Teachers may resist AI tools; investing in training programs and "AI Champion" teacher ambassador network
4. **Regulatory Changes:** AI in education regulations evolving rapidly in SEA; maintaining flexible architecture to adapt to new requirements

---

*This document contains confidential information. Distribution is limited to EduNova Board of Directors and C-suite executives.*
