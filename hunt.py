import ta
import yfinance as yf
import tkinter as tk
from tkinter import ttk
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer

from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer

from reportlab.lib.styles import getSampleStyleSheet

import ta
import yfinance as yf
import tkinter as tk
from tkinter import messagebox, ttk
from tkinter.scrolledtext import ScrolledText
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet

root = tk.Tk()
root.title("Stock Signals App")
def find_single_stock_signal():
    stock_code = single_stock_entry.get().strip().upper()

    try:
        data = yf.download(stock_code, start=start_date, end=end_date)

        if len(data) < 14:
            single_stock_result = f"Not enough data for {stock_code}"
        else:
            rsi = ta.momentum.RSIIndicator(data['Close'], window=14).rsi().iloc[-1]
            upper_band = ta.volatility.BollingerBands(data['Close']).bollinger_hband().iloc[-1]
            lower_band = ta.volatility.BollingerBands(data['Close']).bollinger_lband().iloc[-1]
            macd = ta.trend.MACD(data['Close']).macd().iloc[-1]
            signal = ta.trend.MACD(data['Close']).macd_signal().iloc[-1]

            macd_signal = 'BUY' if macd > signal else 'SELL' if macd < signal else 'NEUTRAL'
            rsi_signal = 'BUY' if rsi < 30 else 'SELL' if rsi > 70 else 'NEUTRAL'
            bollinger_signal = 'BUY' if data['Close'].iloc[-1] < lower_band else 'SELL' if data['Close'].iloc[-1] > upper_band else 'NEUTRAL'

            single_stock_result = f"Stock: {stock_code}\n"
            single_stock_result += f"Latest Date: {data.index[-1].strftime('%Y-%m-%d')}\n"
            single_stock_result += f"Latest MACD Signal: {macd_signal}\n"
            single_stock_result += f"Latest RSI Signal: {rsi_signal}\n"
            single_stock_result += f"Latest Bollinger Bands Signal: {bollinger_signal}"
    except:
        single_stock_result = f"Error fetching data for {stock_code}"

    single_stock_text.config(state=tk.NORMAL)
    single_stock_text.delete('1.0', tk.END)
    single_stock_text.insert(tk.END, single_stock_result)
    single_stock_text.config(state=tk.DISABLED)


# Entry for entering a single stock code
single_stock_label = tk.Label(root, text="Enter Stock Code:")
single_stock_label.pack(pady=5)
single_stock_entry = tk.Entry(root)
single_stock_entry.pack(pady=5)

# Button to find the signals for a single stock
find_single_stock_button = tk.Button(root, text="Find Single Stock Signal", command=find_single_stock_signal)
find_single_stock_button.pack(pady=5)

# Text widget to display the result for a single stock
single_stock_text = ScrolledText(root, height=10, state=tk.DISABLED)
single_stock_text.pack(pady=5)



# Lists of stocks for different sectors
nifty_fmcg_stocks = [
    ('Hindustan Unilever Ltd', 'HINDUNILVR.NS'),
    ('Nestlé India Ltd', 'NESTLEIND.NS'),
    ('ITC Ltd', 'ITC.NS'),
    ('Britannia Industries Ltd', 'BRITANNIA.NS'),
    ('Colgate-Palmolive (India) Ltd', 'COLPAL.NS'),
    ('Godrej Consumer Products Ltd', 'GODREJCP.NS'),
    ('Marico Ltd', 'MARICO.NS'),
    ('Dabur India Ltd', 'DABUR.NS'),
    ('United Spirits Ltd', 'MCDOWELL-N.NS'),
    ('Emami Ltd', 'EMAMILTD.NS')
]

nifty_consumer_durables_stocks = [
    ('Titan Company Ltd', 'TITAN.NS'),
    ('Voltas Ltd', 'VOLTAS.NS'),
    ('Whirlpool of India Ltd', 'WHIRLPOOL.NS'),
    ('Symphony Ltd', 'SYMPHONY.NS'),
    ('TTK Prestige Ltd', 'TTKPRESTIG.NS'),
    ('Crompton Greaves Consumer Electricals Ltd', 'CROMPTON.NS'),
    ('Blue Star Ltd', 'BLUESTARCO.NS'),
    ('Relaxo Footwears Ltd', 'RELAXO.NS'),
    ('VIP Industries Ltd', 'VIPIND.NS'),
    ('Page Industries Ltd', 'PAGEIND.NS')
]

nifty_it_stocks = [
    ('Tata Consultancy Services Ltd', 'TCS.NS'),
    ('Infosys Ltd', 'INFY.NS'),
    ('Wipro Ltd', 'WIPRO.NS'),
    ('HCL Technologies Ltd', 'HCLTECH.NS'),
    ('Tech Mahindra Ltd', 'TECHM.NS'),
    ('Mphasis Ltd', 'MPHASIS.NS'),
    ('MindTree Ltd', 'MINDTREE.NS'),
    ('L&T Infotech Ltd', 'LTI.NS'),
    ('Coforge Ltd', 'COFORGE.NS'),
    ('Tata Elxsi Ltd', 'TATAELXSI.NS')
]

nifty_energy_stocks = [
    ('Reliance Industries Ltd', 'RELIANCE.NS'),
    ('Oil and Natural Gas Corporation Ltd', 'ONGC.NS'),
    ('Indian Oil Corporation Ltd', 'IOC.NS'),
    ('GAIL (India) Ltd', 'GAIL.NS'),
    ('Bharat Petroleum Corporation Ltd', 'BPCL.NS'),
    ('Coal India Ltd', 'COALINDIA.NS'),
    ('Tata Power Company Ltd', 'TATAPOWER.NS'),
    ('Power Grid Corporation of India Ltd', 'POWERGRID.NS'),
    ('NTPC Ltd', 'NTPC.NS'),
    ('Oil India Ltd', 'OIL.NS')
]

nifty_banking_stocks = [
    ('HDFC Bank Ltd', 'HDFCBANK.NS'),
    ('ICICI Bank Ltd', 'ICICIBANK.NS'),
    ('State Bank of India', 'SBIN.NS'),
    ('Kotak Mahindra Bank Ltd', 'KOTAKBANK.NS'),
    ('Axis Bank Ltd', 'AXISBANK.NS'),
    ('IndusInd Bank Ltd', 'INDUSINDBK.NS'),
    ('Bandhan Bank Ltd', 'BANDHANBNK.NS'),
    ('IDFC First Bank Ltd', 'IDFCFIRSTB.NS'),
    ('RBL Bank Ltd', 'RBLBANK.NS'),
    ('Federal Bank Ltd', 'FEDERALBNK.NS')
]

nifty_pharma_stocks = [
    ('Sun Pharmaceutical Industries Ltd', 'SUNPHARMA.NS'),
    ('Dr. Reddy\'s Laboratories Ltd', 'DRREDDY.NS'),
    ('Divi\'s Laboratories Ltd', 'DIVISLAB.NS'),
    ('Cipla Ltd', 'CIPLA.NS'),
    ('Lupin Ltd', 'LUPIN.NS'),
    ('Aurobindo Pharma Ltd', 'AUROPHARMA.NS'),
    ('Biocon Ltd', 'BIOCON.NS'),
    ('Cadila Healthcare Ltd', 'CADILAHC.NS'),
    ('Torrent Pharmaceuticals Ltd', 'TORNTPHARM.NS'),
    ('Alkem Laboratories Ltd', 'ALKEM.NS')
]

nifty_vehicles_stocks = [
    ('Maruti Suzuki India Ltd', 'MARUTI.NS'),
    ('Mahindra & Mahindra Ltd', 'M&M.NS'),
    ('Tata Motors Ltd', 'TATAMOTORS.NS'),
    ('Bajaj Auto Ltd', 'BAJAJ-AUTO.NS'),
    ('Hero MotoCorp Ltd', 'HEROMOTOCO.NS'),
    ('Eicher Motors Ltd', 'EICHERMOT.NS'),
    ('TVS Motor Company Ltd', 'TVSMOTOR.NS'),
    ('Ashok Leyland Ltd', 'ASHOKLEY.NS'),
    ('Motherson Sumi Systems Ltd', 'MOTHERSUMI.NS'),
    ('Balkrishna Industries Ltd', 'BALKRISIND.NS')
]

# ... (Add stock lists for other sectors)

# Organize stocks by sectors
sectors = {
    'FMCG': nifty_fmcg_stocks,
    'Consumer Durables': nifty_consumer_durables_stocks,
    'IT': nifty_it_stocks,
    'Energy': nifty_energy_stocks,
    'Banking': nifty_banking_stocks,
    'Pharma': nifty_pharma_stocks,
    'Vehicles': nifty_vehicles_stocks,
}

# Define the date range
start_date = '2023-01-01'
end_date = '2023-08-01'

# Create the main GUI window


# Create a Treeview widget to display the result data
columns = ("Stock", "Latest Date", "MACD Signal", "RSI Signal", "Bollinger Bands Signal")
treeview = ttk.Treeview(root, columns=columns, show="headings")
for col in columns:
    treeview.heading(col, text=col)
treeview.pack(fill=tk.BOTH, expand=True)

def fetch_and_display():
    treeview.delete(*treeview.get_children())

    for sector, sector_stocks in sectors.items():
        for stock_name, stock_code in sector_stocks:
            data = yf.download(stock_code, start=start_date, end=end_date)

            if len(data) < 14:
                continue

            rsi = ta.momentum.RSIIndicator(data['Close'], window=14).rsi().iloc[-1]
            upper_band = ta.volatility.BollingerBands(data['Close']).bollinger_hband().iloc[-1]
            lower_band = ta.volatility.BollingerBands(data['Close']).bollinger_lband().iloc[-1]
            macd = ta.trend.MACD(data['Close']).macd().iloc[-1]
            signal = ta.trend.MACD(data['Close']).macd_signal().iloc[-1]

            macd_signal = 'BUY' if macd > signal else 'SELL' if macd < signal else 'NEUTRAL'
            rsi_signal = 'BUY' if rsi < 30 else 'SELL' if rsi > 70 else 'NEUTRAL'
            bollinger_signal = 'BUY' if data['Close'].iloc[-1] < lower_band else 'SELL' if data['Close'].iloc[-1] > upper_band else 'NEUTRAL'

            treeview.insert("", "end", values=(stock_name, data.index[-1].strftime('%Y-%m-%d'), macd_signal, rsi_signal, bollinger_signal))

styles = getSampleStyleSheet()

def generate_pdf():
    doc = SimpleDocTemplate("stock_signals.pdf", pagesize=letter)
    story = []

    title = "Stock Signals Report"
    story.append(Paragraph(title, styles["title"]))

    table_data = []
    table_data.append(["Stock", "Sector", "Latest Date", "MACD Signal", "RSI Signal", "Bollinger Bands Signal"])

    for sector, sector_stocks in sectors.items():
        for stock_name, stock_code in sector_stocks:
            data_row = [stock_name, sector]

            data = yf.download(stock_code, start=start_date, end=end_date)

            if len(data) < 14:  # Check if enough data is available for RSI calculation
                print(f"Not enough data for {stock_name}")
                continue

            rsi = ta.momentum.RSIIndicator(data['Close'], window=14).rsi().iloc[-1]
            upper_band = ta.volatility.BollingerBands(data['Close']).bollinger_hband().iloc[-1]
            lower_band = ta.volatility.BollingerBands(data['Close']).bollinger_lband().iloc[-1]
            macd = ta.trend.MACD(data['Close']).macd().iloc[-1]
            signal = ta.trend.MACD(data['Close']).macd_signal().iloc[-1]

            macd_signal = 'BUY' if macd > signal else 'SELL' if macd < signal else 'NEUTRAL'
            rsi_signal = 'BUY' if rsi < 30 else 'SELL' if rsi > 70 else 'NEUTRAL'
            bollinger_signal = 'BUY' if data['Close'].iloc[-1] < lower_band else 'SELL' if data['Close'].iloc[-1] > upper_band else 'NEUTRAL'

            # Apply color to text based on signals
            color_mapping = {'BUY': colors.green, 'SELL': colors.red, 'NEUTRAL': colors.black}
            macd_signal_color = color_mapping[macd_signal]
            rsi_signal_color = color_mapping[rsi_signal]
            bollinger_signal_color = color_mapping[bollinger_signal]

            # Extend data_row with styled text
            data_row.extend([
                data.index[-1].strftime('%Y-%m-%d'),
                macd_signal,
                rsi_signal,
                bollinger_signal
            ])

            table_data.append(data_row)

    table = Table(table_data)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        # ... (rest of the styling)
    ]))

    story.append(table)
    story.append(Spacer(1, 0.2 * inch))

    doc.build(story)

# Create and configure the fetch button
fetch_button = ttk.Button(root, text="Fetch Signals", command=fetch_and_display)
fetch_button.pack()

# Create and configure the generate PDF button
pdf_button = ttk.Button(root, text="Generate PDF", command=generate_pdf)
pdf_button.pack()


# Start the GUI event loop
root.mainloop()