Sudeep Kakade · MS ECE @ Rutgers University
Python · Hardware Validation · Test Automation · Server Infrastructure

This repository contains Python-based hardware validation frameworks and automation tools developed during 3 years of industry experience at Capgemini, where I built validation systems for large-scale cloud server fleets — and extended through academic research at Rutgers.

Background
At Capgemini (Sept 2022 – Aug 2025), I worked on cloud infrastructure hardware validation — building automated frameworks to detect and isolate CPU and memory faults across large-scale server fleets. This work reduced hardware debug time by 80% and ensured hardware integrity prior to production deployment.
The scripts and frameworks in this repository reflect real-world hardware validation engineering: system-level health checks, fault isolation workflows, regression automation, and golden reference modeling.

Projects
1. CPU & Memory Fault Detection Framework
Hardware validation suite for large-scale server fleet fault isolation
ProblemManual fault isolation across hundreds of servers was slow and error-proneSolutionAutomated Python framework to detect and isolate CPU and memory faultsImpact80% reduction in hardware debug timeScopeCPU fault detection · memory fault isolation · automated failure workflow
Key techniques: Parallel health check execution · fault classification · automated reporting

2. System-Level Hardware Health Check Suite
Distributed validation across CPU, memory, storage, and drives
PurposeEnsure hardware integrity across all subsystems prior to production deploymentCoverageCPU · memory · storage · drives — full system validation sweepDeploymentRun as pre-production gate across cloud server fleet
Key techniques: Modular subsystem validators · pass/fail reporting · deployment gating

3. DNN Golden Reference Model
Python/NumPy bit-accurate reference for RTL verification (WINLAB, 2026)
PurposeGenerate test vectors and bit-accurately validate RTL outputs against software baselineContextPart of WINLAB project: converting a pretrained DNN to synthesizable SystemVerilogMethodPython/NumPy golden model → test vector generation → RTL output comparisonResultFunctional correctness validation of RTL inference engine against software DNN
Key techniques: Bit-accurate modeling · test vector generation · RTL-software co-validation

Skills Demonstrated
DomainTools & ConceptsValidation AutomationFault detection · health checks · regression frameworks · automated reportingHardware DomainsCPU · memory · storage · DRAM · server infrastructureRTL Co-VerificationGolden reference modeling · test vector generation · bit-accurate comparisonLanguagesPython · NumPy · Bash · TCLWorkflowGit · Linux · CI-style regression pipelines

Industry Context
These tools were built for production cloud infrastructure validation — not toy examples. The workflows mirror what silicon validation and bring-up teams do at companies like Intel, AMD, Qualcomm, and Google:

Pre-silicon: RTL simulation with Python-generated test vectors
Post-silicon: Hardware bring-up with automated fault detection
Production gate: System-level health checks before server deployment


Author
Sudeep Babasaheb Kakade
MS ECE · Rutgers University · GPA 3.75
LinkedIn · GitHub · saikakade501@gmail.com

🎯 Seeking Fall 2026 / Spring 2027 co-op in Design Verification or RTL Design for SoC/ASIC teams.
