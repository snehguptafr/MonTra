# MonTra
**MonTra** is a simple yet efficient CLI-Based Finance Tracker based on Python. Easily track your incomes and expenses with just a few commands.

#### Features
  - Intuitive and easy command structure.
  - Command Line Interface for high performance with low power consumption.
  - Data Visualisation of your incomes and expenses.
  - Uses Python's powerful data analysis and visualisation libraries.
  - Uses CSV files for facilitating data manipulation and data storage.
  - Platform Independent.
  - Free and Open Source Software.
  - Lightweight.

#### Python Libraries Used
The following Python Libraries(external) are used in MonTra -
 - **Pandas** - to carry out major data manipulation tasks.
Install Pandas - `pip install pandas`
 - **NumPy** - to carry out basic data manipulation tasks.
Install NumPy - `pip install NumPy`
 - **Matplotlib** - for data visualisation.
Install Matplotib - `pip install matplotlib`
 - **Tabulate** - to render DataFrame in MySQL table format.
Install Tabulate - `pip install tabulate`

#### List of Commands

*Note
1: Commands are same for both the editions - Household and Enterprise.
2: MonTra commands are case-sensitive, be careful while typing any commands.*

| Command Structure | Usage | Example |
|-------------------|-------|---------|
| table_name : Month : Category = amount | entering the value | `income : Apr : Sales = 101` |
| table_name : Month : Category + amount | editing the value by adding | `income : Apr : Sales + 101` |
| table_name : Month : Category - amount | editing the value by subtracting | `income : Apr : Sales - 101`
| table_name : Month : Category * amount | editing the value by multiplying | `income : Apr : Sales * 101`
| table_name : Month : Category / amount | editing the value by dividing | `income : Apr : Sales / 101`

*WARNING
1: month and category should be capitalised as shown in the example below and separation from spaces and colon is required.
2: use the amount editing/updating commands only if there is some value existing in a given month and category, do not use it on NaN.*

| Commands | Function |
| ------ | ------ |
| `new session` | Creates a new session by resetting all data |
| `avg tables` | Shows the annual average of all incomes and expenses |
| `avg income plot` | Plots annual average of all incomes |
| `avg expense plot` | Plots annual average of all expenses |
| `plot` | Observe the trends of income and/or expense categories |
| `help` | Shows this help |
| `show` | Shows the Income and Expense Tables |
| `save` | Saves the changes in Income and Expense tables |
| `exit` | Asks to save the changes in Income and Expense tables and exits MonTra |
| `credits` | Shows the name of the developers |

#### License
**Creative Commons Zero v1.0 Universal**

#### Version
**1.0.0**