# AMD Versal™ Prime Series VMK180 Evaluation Kit

![VMK180](./VMK180.jpeg)

## Versal ACAP Core Components

| Component | Description | Function |
|-----------|-------------|----------|
| Scalar Engines | Dual-core Arm Cortex-A72(APU) + Dual-core Cortex-R5F(RPU) | Application processing, real-time control |
| Adaptable Engines | Programmable Logic (CLBs, DSP58, BRAM, UltraRAM) | Custom hardware acceleration |
| Network-on-Chip (NoC) | Programmable multi-terabit interconnect | Data movement between engines |
| Integrated IP | PCIe, Ethernet, DDR controllers, crypto | Standard interface support |

### Scalar Engines (Processing System (PS)):
    *Application Processing Unit* (APU): Dual-core Arm® Cortex®-A72 - processor designed for complex applications running on an operating system like Linux.

    *Real-Time Processing Unit* (RPU): Dual-core Arm Cortex-R5F - processor optimized for low-latency, deterministic control tasks.

    *Platform Management Controller* (PMC): Dedicated processor for handling device management/debugging, security, and boot

### Adaptable Engines (Programmable Logic (PL)):
This is the traditional "FPGA" portion, featuring roughly 1.3M to 1.9M system logic cells (depending on the specific silicon revision) for custom hardware acceleration. 

An *Field-Programmable Gate Array* (FPGA) is an integrated circuit that can be programmed after manufacturing to implement custom digital hardware.

Unlike a normal processor that runs software instructions, an FPGA lets you configure the hardware itself to perform specific tasks. Key Idea is that an FPGA contains thousands or millions of configurable logic blocks and programmable interconnections. By programming these connections, you can create custom digital circuits.

Think of it as building your own hardware chip using software tools.

### Programmable Network-on-Chip (NoC): 
This is the "glue" of the architecture. It provides a multi-terabit interconnect that allows data to move between the processing system, memory controllers, and programmable logic without consuming traditional routing resources.

### Intelligent Engines:
DSP Engines: High-precision floating-point and fixed-point processing.
the DSP (Digital Signal Processing) engines are known as DSP58 slices. They are the "math powerhouses" of the programmable logic, specifically designed to handle high-precision arithmetic that would be too slow or power-hungry for the ARM processors to do alone.

## System Infrastructure
The architecture is tied together by high-performance internal and external interconnects: 

    Programmable Network on Chip (NoC): An optimized multi-terabit interconnect that provides high-bandwidth paths between the compute engines, memory controllers, and I/O.
    
    Integrated Shell: A pre-built system infrastructure that allows designers to jump-start development without building basic connectivity from scratch.
    
    Integrated DDR Controllers: Hardened controllers that support DDR4 and LPDDR4 memory interfaces for efficient data handling

