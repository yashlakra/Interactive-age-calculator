# Life Analytics & Age Calculator Suite

A collection of interactive Python utilities for calculating age, analyzing life statistics, and exploring zodiac signs with detailed breakdowns and insights.

## Features

### 🎂 Interactive Age Calculator
- Multiple input methods: birthdate (YYYY-MM-DD) or age components (years/months/days)
- Precise age breakdown: years, months, days, hours, minutes, seconds
- Total time calculations in days and seconds
- Leap year detection and listing between birth year and current year
- Input validation with helpful error messages
- Interactive CLI with repeat functionality

### 🌌 Life Analytics System (Zodiac)
- Comprehensive life report generation
- Zodiac sign calculation based on birthdate
- Next birthday countdown
- Estimated heartbeat counter
- Life milestone tracking (10, 20, 30, 40, 50 years)
- Interactive menu system with multiple viewing options
- Personalized reports with user name

### 🧪 JavaScript Playground
- Practice code for JavaScript fundamentals
- Switch case statement examples
- Array manipulation and functional programming patterns

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd <repository-name>
```

2. Ensure Python 3.7+ is installed:
```bash
python --version
```

3. No external dependencies required - uses Python standard library only!

## Usage

### Interactive Age Calculator

```bash
python "Interactive age calculator.py"
```

Follow the interactive prompts to:
- Enter your name
- Choose input method (birthdate or age components)
- View detailed age breakdown
- Perform multiple calculations

Example output:
```
========================================
Hello, John! Here's a detailed breakdown of your age:
----------------------------------------
Age: 34 years, 5 months, 12 days, 8 hours, 23 minutes, 45 seconds
Total: 12,580 days (1,086,912,000 seconds)
----------------------------------------
Leap years between 1989 and 2024 (9): 1992, 1996, 2000, 2004, 2008, 2012, 2016, 2020, 2024
========================================
```

### Life Analytics System

```bash
python "ZODIAC shit.py"
```

Navigate through the menu to:
1. View full life report with all statistics
2. Check zodiac sign only
3. See days until next birthday
4. Exit program

Example output:
```
============================================================
📊 LIFE ANALYSIS REPORT FOR: JOHN DOE
============================================================
🎂 Birthday            : 1989-03-15
🧓 Age in Years        : 34
📆 Age in Months       : 413
⏳ Age in Days         : 12,580
♈ Zodiac Sign         : Pisces
🎉 Next Birthday       : 2025-03-15 (22 days left)
❤️ Estimated Heartbeats: 1,304,064,000

🏅 LIFE MILESTONES:
 - 🎉 You have lived over 10 years!
 - 🏆 Two decades of memories!
 - 🔥 30 Years Strong!
```

### JavaScript Playground

Open `JS/index.html` in a browser or run the JavaScript file with Node.js:

```bash
node JS/Playground.js
```

## Project Structure

```
.
├── Interactive age calculator.py  # Precise age calculator with multiple input methods
├── ZODIAC shit.py                # Life analytics with zodiac and milestones
├── JS/
│   ├── Playground.js             # JavaScript practice code
│   └── index.html                # HTML wrapper for JS playground
├── Mini project/                 # macOS window resizer projects (Swift)
├── README.md                     # This file
└── requirements.txt              # Python dependencies
```

## Technical Details

### Age Calculation Algorithm
- Handles leap years correctly (Feb 29 edge cases)
- Accounts for varying month lengths
- Precise time-of-day calculations
- Validates future dates and invalid inputs

### Zodiac Sign Calculation
- Based on astronomical dates
- Covers all 12 zodiac signs
- Accurate date range matching

### Input Validation
- Regex-based date parsing
- Range validation for numeric inputs
- User-friendly error messages
- Graceful handling of edge cases

## Requirements

- Python 3.7 or higher
- Standard library modules only (no pip install needed):
  - `datetime`
  - `calendar`
  - `re`
  - `sys`

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the MIT License.

## Author

Created with ❤️ for exploring time, life, and the cosmos.

## Future Enhancements

- [ ] Add Chinese zodiac calculation
- [ ] Export reports to PDF/CSV
- [ ] Web interface using Flask/Django
- [ ] Add more life milestones and fun facts
- [ ] Integration with calendar APIs
- [ ] Visualization of life timeline
- [ ] Multi-language support

## Support

For issues, questions, or suggestions, please open an issue on GitHub.

---

**Note**: The JavaScript playground and macOS window resizer projects are separate utilities included in this repository for convenience.
