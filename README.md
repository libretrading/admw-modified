# admw-modified

Welcome to the `admw-modified` repository! This open-source trading strategy is a Modified Accelerated Dual Momentum Weekly Portfolio Strategy with Filters, applied to a diversified set of ETFs. This strategy helps investors achieve optimal portfolio allocation using momentum-based signals and weekly adjustments.

---

## Strategy Overview

### Key Indicators
1. **Momentum (Rates of Change)**
   - Uses 21-day, 63-day, and 126-day rates of change (ROC) to calculate momentum for each ETF.
   - Averages these values to create a robust signal.

2. **Weekly Adjustments**
   - Trading decisions are made on the last trading day of each week.
   - Positions are updated based on calculated momentum values.

3. **Filters**
   - Includes safety assets (e.g., TLT, UUP) to switch to during weak equity momentum.

### Signal Logic
- **Long Equities:** Choose the equity asset with the highest positive momentum (e.g., QQQE or EFA).
- **Short Term Treasury Filter:** equity assets not only need to show positive returns but higher returns than IEI
- **Safety Assets:** If equity momentum is weak, choose the safety asset with the highest momentum (e.g., TLT or UUP).
- **Flat:** Maintain no position if no assets meet the criteria.

### Backtesting and Performance
- Calculates daily equity based on momentum-based signals.
- Generates a continuous equity curve for visualization.
- Starts with an initial balance of $10,000.

---

## Installation and Usage

### Prerequisites
Ensure you have the following Python libraries installed:
- `numpy`
- `pandas`
- `yfinance`
- `matplotlib`

Install missing dependencies with:
```bash
pip install numpy pandas yfinance matplotlib
```

### Running the Strategy
1. Clone the repository:
   ```bash
   git clone https://github.com/LibreTrading/admw-modified.git
   cd admw-modified
   ```

2. Run the Python script:
   ```bash
   python admw_modified_strategy.py
   ```

The script will:
- Download historical price data for the specified ETFs.
- Calculate momentum signals and determine weekly positions.
- Generate a plot of the equity curve and display key metrics.

---

## Features
- **Momentum Calculations:** Computes ROC-based momentum for each asset.
- **Weekly Adjustments:** Implements logic for weekly portfolio rebalancing.
- **Visualization:** Plots positions and equity curves for transparency.
- **Performance Metrics:** Outputs the final equity value after backtesting.

---

## Contributions
We welcome contributions from the community! Feel free to:
- Open issues for bugs or feature requests.
- Submit pull requests to improve the strategy or code quality.

---

## Credit
This strategy builds upon the Accelerated Dual Momentum concept published by Swhanly from [EngineeredPortfolio.com](https://engineeredportfolio.com), based on Gary Antonacci's original Dual Momentum framework. We modified the frequency to weekly, applied it to different ETFs, and added additional filters.

---

## Support
If you need help automating this strategy, visit [Plutarco](https://plutarco.tech)

---

## License
This project is open-source under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Donations
Support the LibreTrading community by contributing to the project. Every donation helps us continue to develop and share open-source trading tools.

Thank you for being part of the LibreTrading community!
