from Mathematics.Summation.Sigma_Power import sigma_form

# TODO expand to non natural powers
if __name__ == "__main__":
    for i in range(100):
        print("S({}) = {}".format(i, "+".join(" {} x^{}".format(v, i + 1) for i, v in enumerate(sigma_form(i)))))
