# import flask
from flask import Flask, url_for

# import jinja template engine
from flask import render_template

from flask import request, jsonify

import random

# create an app instance
app = Flask(__name__);

# Model

questions = [
   {
     "id": 1,
     "title": "IPO stands for:",
     "options": [
      {
        "value": "Itemized Public Organization",
        "is_correct": False
      },
      {
        "value": "Initial Primary Offering",
        "is_correct": False
      },
      {
        "value": "Initial Public Offering",
        "is_correct": True
      },
      {
        "value": "Imminent Profitable Option",
        "is_correct": False
      }
     ],
   },
   {
     "id": 2,
     "title": "Which asset determines the ownership of the company:",
     "options": [
      {
        "value": "Real Estate",
        "is_correct": False
      },
      {
        "value": "Stocks",
        "is_correct": True
      },
      {
        "value": "Loan",
        "is_correct": False
      },
      {
        "value": "Bonds",
        "is_correct": False
      }
     ],
   },
   {
     "id": 3,
     "title": "New York Stock Exchange or Nasdaq refer to:",
     "options": [
      {
        "value": "Primary market",
        "is_correct": False
      },
      {
        "value": "Farm market",
        "is_correct": False
      },
      {
        "value": "Exchange market",
        "is_correct": False
      },
      {
        "value": "Secondary market",
        "is_correct": True
      }
     ],
   },
   {
     "id": 4,
     "title": "This characteristic is related to equity:",
     "options": [
      {
        "value": "Pay dividend",
        "is_correct": True
      },
      {
        "value": "Has a maturity date",
        "is_correct": False
      },
      {
        "value": "Only traded on secondary market",
        "is_correct": False
      },
      {
        "value": "Return on investment is guaranteed",
        "is_correct": False
      }
     ],
   },
   {
     "id": 5,
     "title": "Reward, cash or otherwise, that a company gives to its shareholders",
     "options": [
      {
        "value": "Coupon payments",
        "is_correct": False
      },
      {
        "value": "Interest payment on a loan",
        "is_correct": False
      },
      {
        "value": "Dividend",
        "is_correct": True
      },
      {
        "value": "None of the above",
        "is_correct": False
      }
     ],
   },
   {
     "id": 6,
     "title": "Does a bondholder get a principal amount?",
     "options": [
      {
        "value": "Yes, when a company pays dividends",
        "is_correct": False
      },
      {
        "value": "Yes, when a company pays coupon payment",
        "is_correct": False
      },
      {
        "value": "Yes, when bond matures",
        "is_correct": True
      },
      {
        "value": "No, a company does not guarantee a principal amount",
        "is_correct": False
      }
     ],
   },
   {
     "id": 7,
     "title": "When a market is volatile, an investor expects predictable income stream from:",
     "options": [
      {
        "value": "Bonds",
        "is_correct": True
      },
      {
        "value": "Loan",
        "is_correct": False
      },
      {
        "value": "Cryptocurrency",
        "is_correct": False
      },
      {
        "value": "Stocks",
        "is_correct": False
      }
     ],
   },
   {
     "id": 8,
     "title": "When a company can't pay the interest or principal in a timely manner or at all, this\
event happens:",
     "options": [
      {
        "value": "Market value risk",
        "is_correct": False
      },
      {
        "value": "Default risk",
        "is_correct": True
      },
      {
        "value": "Liquidity risk",
        "is_correct": False
      },
      {
        "value": "Inflation risk",
        "is_correct": False
      }
     ],
   },
   {
     "id": 9,
     "title": "As a bondholder you have following benefits and rights:",
     "options": [
      {
        "value": "Voting rights in a company",
        "is_correct": False
      },
      {
        "value": "Carry ownership interest",
        "is_correct": False
      },
      {
        "value": "Receive repayment of principal at maturity date",
        "is_correct": True
      },
      {
        "value": "Don’t have a guarantee on investment return",
        "is_correct": False
      }
     ],
   },
   {
     "id": 10,
     "title": "Define bond origination:",
     "options": [
      {
        "value": "Principal repayment at maturity date",
        "is_correct": False
      },
      {
        "value": "Receive coupon payments",
        "is_correct": False
      },
      {
        "value": "Purchase bonds on IPO",
        "is_correct": False
      },
      {
        "value": "The act of making loan",
        "is_correct": True
      }
     ],
   },
   {
     "id": 11,
     "title": "The secondary market is:",
     "options": [
      {
        "value": "Occurs when a private company issues stock to the public for the first time",
        "is_correct": False
      },
      {
        "value": "A market where bond origination happens",
        "is_correct": False
      },
      {
        "value": "A market where investors buy and sell securities they already own",
        "is_correct": True
      },
      {
        "value": "None of the above",
        "is_correct": False
      }
     ],
   },
   {
     "id": 12,
     "title": "Diversification in stock investments:",
     "options": [
      {
        "value": "Leads to a default risk",
        "is_correct": False
      },
      {
        "value": "Mitigates a risk of losing all money",
        "is_correct": True
      },
      {
        "value": "Help to get voting rights in a company",
        "is_correct": False
      },
      {
        "value": "Mitigates an inflation risk",
        "is_correct": False
      }
     ],
   },
   {
     "id": 13,
     "title": "The coupon payment has following characteristics:",
     "options": [
      {
        "value": "An interest paid only at maturity date",
        "is_correct": False
      },
      {
        "value": "A company cannot guarantee a coupon payment",
        "is_correct": False
      },
      {
        "value": "Gives a voting right in a company",
        "is_correct": False
      },
      {
        "value": "None of the above",
        "is_correct": True
      }
     ],
   },
   {
     "id": 14,
     "title": "Owner of stock in a company or corporation:",
     "options": [
      {
        "value": "Portfolio",
        "is_correct": False
      },
      {
        "value": "Shareholder",
        "is_correct": True
      },
      {
        "value": "Industry",
        "is_correct": False
      },
      {
        "value": "Stock market",
        "is_correct": False
      }
     ],
   },
   {
     "id": 15,
     "title": "You can buy stock in any company in the world:",
     "options": [
      {
        "value": "True, all companies are required to offer stock",
        "is_correct": False
      },
      {
        "value": "True, you can buy stock on Nasdaq",
        "is_correct": False
      },
      {
        "value": "False, a company has to go to IPO first",
        "is_correct": True
      },
      {
        "value": "False, not all stocks are offered on New York Stock Exchange",
        "is_correct": False
      }
     ],
   },
   {
     "id": 16,
     "title": "Company can obtain capital through:",
     "options": [
      {
        "value": "Issuing stocks and offering it on IPO",
        "is_correct": False
      },
      {
        "value": "Issuing bonds",
        "is_correct": False
      },
      {
        "value": "Bank loan only",
        "is_correct": False
      },
      {
        "value": "Issuing both stocks and bonds",
        "is_correct": True
      }
     ],
   },

];

# create a base route
@app.route('/')

# create home method
def home():
  return render_template('main.html')

# create a base route
@app.route('/stocks1')

# create home method
def stocks1():
  return render_template('stocks1.html')

# create a base route
@app.route('/stocks2')

# create home method
def stocks2():
  return render_template('stocks2.html')

# create a base route
@app.route('/stocks3')

# create home method
def stocks3():
  return render_template('stocks3.html')

# create a base route
@app.route('/stocks4')

# create home method
def stocks4():
  return render_template('stocks4.html')

# create a base route
@app.route('/bonds1')

# create home method
def bonds1():
  return render_template('bonds1.html')

# create a base route
@app.route('/bonds2')

# create home method
def bonds2():
  return render_template('bonds2.html')

# create a base route
@app.route('/bonds3')

# create home method
def bonds3():
  return render_template('bonds3.html')

# create a base route
@app.route('/bonds4')

# create home method
def bonds4():
  return render_template('bonds4.html')

# create a quiz route
@app.route('/quiz')

# create quiz method
def quiz():
  return render_template('quiz.html')

# get quiz data
@app.route('/quiz-data', methods=['POST'])

def quiz_data():
  global questions

  first = 1
  last = len(questions)

  questionNumbers = random.sample(range(first, last), 10)

  randomQuestions = []
  for qn in questionNumbers:
    randomQuestions.append(questions[qn-1])

  data_to_send = {
    "questions": randomQuestions
  }

  return jsonify(data_to_send)

# create a complete route
@app.route('/result')

def result():
  return render_template('result.html')


  

