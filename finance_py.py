"""The annual percentage yield (APY) is the real rate of return earned on an investment,
taking into account the effect of compounding interest. Unlike simple interest,
compounding interest is calculated periodically and the amount is immediately added to the balance.
"""


def annual_percentage_yield():
    print('--------------------------Annual Percentage Yield----------------------')
    r = float(input('Rate ->'))
    n = float(input('Compounding frequency ->'))
    apy = (1 + (r / 100) / n) ** n - 1
    print("Annual Percentage Yield =>", apy * 100, '%')


'''A balloon loan comprises a stream of constant payments 
followed by a large payment at the end, which is called the balloon payment.
'''


def balloon_loan_payment():
    print('--------------------------Balloon loan payment----------------------')
    '''PV is the present value of Original Balance
    P is the Payment
    r is the rate of interest
    n is the frequency of payments
    PV x (1+r)^n – P x [(1+r)^n – 1 / r]'''

    pv = int(input("Current Bank Balance -> "))
    r = float(input("Rate of Interest ->"))
    n = float(input("Frequency of Payments ->"))
    P = float(input("Enter Payment ->"))

    Fv1 = pv * ((1 + r) ** n)
    Fv2 = P * ((((1 + r) ** n) - 1) / r)
    FV = Fv1 - Fv2
    print("Balloon loan Payment =>", FV)  # (P *(((1+r)**n)1/r))


'''Compound interest is the addition of interest to the principal 
sum of a loan or deposit, or in other words, interest on principal plus interest.
'''


def compound_interest():
    print('--------------------------Compound interest----------------------')
    p = float(input("Enter the Principal amount ->"))
    r = float(input("Enter the Interest rate"))
    n = float(input("Enter number of times Interest applied"))
    A = p * (((1 + r) ** n) - 1)
    print("Compound Interest =>", A)


'''This formula determines the interest that is earned on an amount by 
constantly compounding it to a theoretically infinite amount of compounding periods.
'''


def continuous_compounding():
    print('--------------------------Continuous Compounding----------------------')
    p = float(input("Enter the principle ->"))
    r = float(input("Enter the rate ->"))
    t = float(input("Enter the time ->"))
    e = 2.718
    cont = p * (e ** (r * t))
    print("continuous compounding =>", cont)


'''In addition to your credit score, your debt-to-income (DTI) ratio is an important part of your overall financial
health. Calculating your DTI1 may help you determine how comfortable you are with your current debt, and also decide
whether applying for credit is the right choice for you. '''


# Debt to income ratio

def debt_to_income_ratio():
    print('--------------------------debt to income ratio----------------------')
    annual_income = float(input('Enter annual income ->'))
    monthly_debt = float(input('Enter monthly debt ->'))
    monthly_income = annual_income / 12
    debt_to_income_ratio1 = (monthly_debt / monthly_income) * 100
    print('The debt to income ratio => ', debt_to_income_ratio1, '%')
    if debt_to_income_ratio1 > 35:
        print('Do not take more debt until your ratio has stabilized to below 35%')
    elif debt_to_income_ratio1 < 10:
        print('can take more debt until your ratio has is below 10%')


''' balloon note, is a note that has a term that is shorter than its amortization. 
In other words, the loan payment will be amortized, or calculated, for a certain
amount of years but the loan will be paid off before all payments calculated are made, 
thus leaving a balance due. An example would be a note that is calculated for 30 years, 
but the remaining balance after 10 years must be paid in one full sum. This example is
 commonly referred to as a 10/30 balloon.

'''


def balloon_balance_of_a_loan():
    print('--------------------------Balloon_balance_of_a_loan----------------------')
    Present_Value1 = float(input('Enter amount present in bank(present value). ->'))
    payment1 = float(input('Enter payment (payment). ->'))
    rate_per_payment1 = float(input('Enter rate per payment (rate_per_payment). ->'))
    number_of_payment1 = float(input('Enter number of payment (number_of_payment). ->'))

    Fv1 = Present_Value1 * (1 + rate_per_payment1) ** number_of_payment1
    Fv2 = payment1 * ((((1 + rate_per_payment1) ** number_of_payment1) - 1) / rate_per_payment1)
    Fv = Fv1 - Fv2

    print('Future value = ', Fv)


'''The loan payment formula is used to calculate the payments on a loan.
 The formula used to calculate loan payments is exactly the same as the 
 formula used to calculate payments on an ordinary annuity. A loan, by definition,
  is an annuity, in that it consists of a series of future periodic payments.'''


def loan_payment():
    print('--------------------------Loan Payment----------------------')
    present_value = float(input('Amount present in your bank ->'))
    rate = float(input('Rate per period ->'))
    number_of_periods = float(input('Number of periods ->'))
    rate /= 100

    Pay1 = (rate * present_value)
    Pay2 = 1 - (1.0 + rate) ** (-number_of_periods)
    payment = Pay1 / Pay2
    print('Amount to be paid =>', payment)


'''Loan balance refers to the amount of money you have to repay on your loan.
'''


def balance_on_loan():
    print('--------------------------Balance on loan----------------------')
    present_value = float(input('Amount present in your bank ->'))
    rate = float(input('Rate per payment ->'))
    number_of_payments = float(input('number of payment ->'))
    P = float(input('Payment'))
    Future_payment1 = present_value * ((1 + rate) ** number_of_payments)
    Future_payment2 = P * ((((1 + rate) ** number_of_payments) - 1) / rate)
    Future_payment = Future_payment1 - Future_payment2
    print('Balance of loan to pay =>', Future_payment)


'''The loan to deposit ratio is used to calculate a lending institution's ability 
to cover withdrawals made by its customers. A lending institution that accepts deposits 
must have a certain measure of liquidity to maintain its normal daily operations. Loans given 
to its customers are mostly not considered liquid meaning that they are investments over a longer
 period of time. Although a bank will keep a certain level of mandatory reserves, they may also
  choose to keep a percentage of their non-lending investing in short term securities to ensure
   that any monies needed can be accessed in the short term.
'''


def loan_to_deposit_ratio():
    print('--------------------------loan to deposit ratio----------------------')
    Loan = float(input('Enter your loan amount ->'))
    Deposit = float(input('Enter your Deposit ->'))
    ratio = Loan / Deposit
    print('Loan to Deposit ratio =>', ratio)


''' Simple interest is determined by multiplying the daily interest rate by the
 principal by the number of days that elapse between payments.
'''


def simple_interest(r=7, t=1):  # Simple Interest
    print('--------------------------Simple interest----------------------')
    p = float(input("Enter the Amount present in the Account in Rs. -> "))  # Principal/amount present in bank
    # return amount
    r = float(input("Enter the Rate of Interest in % -> "))  # roi
    t = float(input("Enter the Time period in Years -> "))  # no.of yrs
    simple_i = int((p * r * t) / 100)
    print("Simple Interest => Rs.", simple_i)


'''Net Interest Characteristics:
1. Net interest income (NII) is defined as the difference between interest revenues and interest expenses.
2. Net interest margin (NIM) is a measurement comparing the net interest income a financial
firm generates from credit products like loans and mortgages, with the outgoing
interest it pays holders of savings accounts and certificates of deposits(CDs).
'''


def net_interest_characteristics():
    print('--------------------------Net interest income----------------------')
    ii = int(input("Enter the Interest Income in Rs.-> "))
    ir = int(input("Enter the Rate of Interest on Loans charged -> "))
    IIR = int((ii * ir))
    ie = int(input("Enter the Interest Expenditure in Rs. -> "))
    er = int(input("Enter the Interest gained by providing loans -> "))
    IER = int((ie * er))

    nii = IIR - IER  # Net Interest Income(nii) for a Bank or a Company

    # Net Interest Margin Calculation
    asset_beg = int(input("Enter the assets at the beginning of the Financial Year -> "))
    asset_end = int(input("Enter the assets at the ending of the Financial Year -> "))
    avg_ea = int((asset_beg + asset_end)) / 2
    nim = float((nii / avg_ea)) * 100  # Net Interest Margin
    print("Net Interest Income => ", round(nii, 2))
    print("Net Interest Margin => ", round(nim, 2), "%")


'''Loan-to-value (LTV) is calculated simply by taking the loan
amount and dividing it by the value of the asset or collateral being borrowed against.
'''


def loan_to_value():
    print('--------------------------Loan to value Ratio----------------------')
    l_v = int(input("Enter the Loan Amount/Value in Rs. -> "))
    v_c = int(input("Enter the Value of Collateral in Rs. ->"))
    ltv = (l_v / v_c)
    print("Loan to Value Ratio is => ", ltv)
    if ltv <= 0.05:
        print("Not eligible to avail the loan")
    else:
        print("Hence Eligible for Loan")
