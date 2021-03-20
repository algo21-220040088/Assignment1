import math
import scipy.stats as st
class Option():
    def __init__(self,CallPutFlag,S,X,T,r,b):
        self.CallPutFlag=CallPutFlag
        self.S = S
        self.X = X
        self.T = T
        self.r = r
        self.b = b

    def g_black_scholes(self,v):
        d1 = (math.log(self.S / self.X) + (self.b + (v ** 2) / 2) * self.T) / (v * math.sqrt(self.T))
        d2 = d1 - v * math.sqrt(self.T)
        if self.CallPutFlag == 'c':
            g_black_scholes = self.S * math.exp((self.b - self.r) * self.T) * st.norm.cdf(d1) - self.X * math.exp(-self.r * self.T) * st.norm.cdf(d2)
        elif self.CallPutFlag == 'p':
            g_black_scholes = self.X * math.exp(-self.r * self.T) * st.norm.cdf(-d2) - self.S * math.exp((self.b - self.r) *self.T) * st.norm.cdf(-d1)
        return g_black_scholes

    def vega(self,v):
        d1 = (math.log(self.S / self.X) + (self.b + (v ** 2) / 2) *self.T)/ (v * math.sqrt(self.T))
        vega = self.S * math.exp((self.b - self.r) * self.T) * st.norm.pdf(d1)*math.sqrt(self.T)
        return vega

    def g_implied_volatility_nr(self, cm, epsilon):
        vi = math.sqrt(abs(math.log(self.S / self.X) + self.r * self.T) * 2 / self.T)
        ci = self.g_black_scholes(vi)
        vega_i = self.vega(vi)
        mindiff = abs(cm - ci)
        while abs(cm - ci) >= epsilon and abs(cm - ci) <= mindiff:
            vi = vi - (ci - cm) / vega_i
            ci = self.g_black_scholes( vi)
            vega_i = self.vega(vi)
            mindiff = abs(cm - ci)
        if abs(cm - ci) < epsilon:
            g_implied_volatility_nr = vi
        else:
            g_implied_volatility_nr = 'NA'
        return g_implied_volatility_nr

if __name__=='__main__':
    a=Option('p',59,60,0.25,0.067,0.067)
    y=a.g_implied_volatility_nr(2.82,0.001)
    print(y)
