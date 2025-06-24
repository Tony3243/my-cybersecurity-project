# Cyber Threat Detector log anomolies

This code structute portrays a beginner-friendly Python + Bash that scrutinizes system 
log files to detect suspicious login activity(e.g., repeated failed SSH logins).

## 🔧 Technologies used
- Python 3
- Bash
- Libraries: 'pandas', 'loguru', 're'

## 📁Project Structure
- 'logs/' - contains input '.log' files (e.g., auth logs)
- 'outputs/' - CSV format of IPs suspicious reports
- 'logs_app/ - loguru is speacialized to show the runtime of logs
- 'src'/ - embeded with python source code to orchestrate the detection

## 🔑 How to Run
- '''bash
# Install dependencies
pip install -r requirements.txt

# run the detection script
bash run_detector.sh