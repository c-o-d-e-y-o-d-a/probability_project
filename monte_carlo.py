
from flask import Flask, send_file
import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt
import io
import base64

def exampleFunction(companyName, num_simulations=100):
    df = yf.download(companyName)
    returns = np.log(1 + df['Adj Close'].pct_change())
    mu, sigma = returns.mean(), returns.std()

    fig, ax = plt.subplots()

    for _ in range(num_simulations):
        sim_rets = np.random.normal(mu, sigma, 252)
        initial = df['Adj Close'].iloc[-1]
        sim_prices = initial * (sim_rets + 1).cumprod()
        ax.plot(sim_prices)

    ax.axhline(initial, c='k')
    plt.xlabel('number of days')
    plt.ylabel('price')

    # Save the plot to a BytesIO object
    img_buf = io.BytesIO()
    plt.savefig(img_buf, format='png')
    img_buf.seek(0)

    # Close the plot to avoid memory leaks
    plt.close()

    return img_buf


app = Flask(__name__)

@app.route('/home/<string:companyName>', methods=['GET'])
def disp(companyName):
    img_buf = exampleFunction(companyName)
    return send_file(img_buf, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True, threaded=False)