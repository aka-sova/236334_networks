

# Homework no. 1
## Submission:
- Alexander Shender 328626114
- Edo Agmon XXXXXXXX


## Question #1

### (a)

The following chart shows the structure of the complete frame, where for each layer the according protocol is mentioned and the bytes number

| Layer        | Protocol           | Header size  |
|-|-|-|
| 5 | http | - |
| 4 | TCP | 20 |
| 3 | IPv4 | 20 |
| 2 | MAC + CRC | 14 + 4 |
| 1 | PHY | - |

The following diagram shows it explicitly:

 <img src="imgs/q1_1.png" width="" title="frame structure">

 Thus, total size of the frame that the PHY layer receives is 1558 bytes.

<br/>
<br/>
<br/>

 ### (b)

