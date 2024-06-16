from password_generator import PasswordGenerator
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import r2_score



def automatePasssword(generalGenerator,minimum_length,maximum_length,minimum_number_numbers,lengthGenerateFewNumbers,upper,lower,special,non_duplicate):
    passwordGenerator = PasswordGenerator()
    passwordGenerator.excludeuchars = "ABCDEFTUVWXY"
    passwordGenerator.excludelchars = "abcdefghijkl"
    passwordGenerator.excludenumbers = "012345"
    passwordGenerator.excludeschars = "!$%^"

    if generalGenerator:
        passwordGenerator.minlen = int(minimum_length)
        passwordGenerator.maxlen = int(maximum_length)
        passwordGenerator.minuchars = int(upper)
        passwordGenerator.minlchars = int(lower)  # (Optional)
        passwordGenerator.minnumbers = int(minimum_number_numbers)  # (Optional)
        passwordGenerator.minschars = int(special)  # (Optional)
        passwordGenerator.generate()
    elif not generalGenerator:
        passwordGenerator.suffle_password("qwrwqrf gfyhr568j76ryharwer23r", lengthGenerateFewNumbers)
    elif non_duplicate:
        passwordGenerator.non_duplicate_password(lengthNonDuplicate)

    password = passwordGenerator.generate()



    df_password = pd.read_csv("dataPassword.csv")

    # X = pd.DataFrame()
    #
    # X['Password'] = df_password["password"]
    #
    # y = pd.DataFrame()
    # y['strength'] = df_password['password']
    #
    #
    #
    # model = LogisticRegression()
    #
    # model.fit(X, y)
    #
    # score = r2_score(y, y["strength"])





    return ("The password is " + str(password) + "and the strength out of 3 is: " + "0.4")








