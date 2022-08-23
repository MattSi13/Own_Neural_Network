"""
This script allows you to add to your dataset all the technical indicators of the Talib library.
"""

# Indicators from talib
import warnings  # to ignore warnings messages

warnings.filterwarnings('ignore')


def talib_function(dataframe, talib):  # talib => add like argument the talib library

    # 1) Overlap studies function

    # DEMA
    dataframe['DEMA'] = talib.DEMA(dataframe.Close, timeperiod=30)

    # Add BBANDS : helps to point out the buy and sell signals
    dataframe['upperband'], dataframe['middleband'], dataframe[
        'lowerband'] = talib.BBANDS(dataframe.Close,
                                    timeperiod=5,
                                    nbdevup=2,
                                    nbdevdn=2,
                                    matype=0)

    # Add EMA200 : : used to identify the predominant trend in the market
    #dataframe['EMA200'] = talib.EMA(dataframe.Close, timeperiod=200)

    # Add EMA99
    dataframe['EMA99'] = talib.EMA(dataframe.Close, timeperiod=99)

    # Add EMA50
    #dataframe['EMA50'] = talib.EMA(dataframe.Close, timeperiod=50)

    # Add EMA20
    #dataframe['EMA20'] = talib.EMA(dataframe.Close, timeperiod=20)

    # Add EMA7
    #dataframe['EMA7'] = talib.EMA(dataframe.Close, timeperiod=7)

    # Add HT_TRENDLINE
    dataframe['HT_TRENDLINE'] = talib.HT_TRENDLINE(dataframe.Close)

    # Add KAMA
    dataframe['KAMA'] = talib.KAMA(dataframe.Close, timeperiod=30)

    # Add MA
    dataframe['MA'] = talib.MA(dataframe.Close, timeperiod=30, matype=0)

    # Add MAMA (doesnt work)
    #dataframe['MAMA'], dataframe['FAMA'] = talib.MAMA(dataframe.Close, fastlimit=0, slowlimit=0)

    # Add MIDPOINT
    dataframe['MIDPOINT'] = talib.MIDPOINT(dataframe.Close, timeperiod=14)

    # Add MIDPRICE
    dataframe['MIDPRICE'] = talib.MIDPRICE(dataframe.High,
                                           dataframe.Low,
                                           timeperiod=14)

    # Add SAR
    dataframe['SAR'] = talib.SAR(dataframe.High,
                                 dataframe.Low,
                                 acceleration=0,
                                 maximum=0)

    # Add SAREXT
    dataframe['SAREXT'] = talib.SAREXT(dataframe.High,
                                       dataframe.Low,
                                       startvalue=0,
                                       offsetonreverse=0,
                                       accelerationinitlong=0,
                                       accelerationlong=0,
                                       accelerationmaxlong=0,
                                       accelerationinitshort=0,
                                       accelerationshort=0,
                                       accelerationmaxshort=0)

    # Add SMA20
    dataframe['SMA20'] = talib.SMA(dataframe.Close, timeperiod=20)

    # Add SMA50
    dataframe['SMA50'] = talib.SMA(dataframe.Close, timeperiod=50)

    # Add SMA200
    dataframe['SMA200'] = talib.SMA(dataframe.Close, timeperiod=200)

    # Add T3
    dataframe['T3'] = talib.T3(dataframe.Close, timeperiod=5, vfactor=0)

    # Add TEMA
    dataframe['TEMA'] = talib.TEMA(dataframe.Close, timeperiod=30)

    # Add TRIMA
    dataframe['TRIMA'] = talib.TRIMA(dataframe.Close, timeperiod=30)

    # Add WMA
    dataframe['WMA'] = talib.WMA(dataframe.Close, timeperiod=30)

    # 2) Momentum Indicators

    # Add ADX : identify the strength of a trend
    dataframe['ADX'] = talib.ADX(dataframe.High,
                                 dataframe.Low,
                                 dataframe.Close,
                                 timeperiod=14)

    # Add ADXR
    dataframe["ADXR"] = talib.ADXR(dataframe.High,
                                   dataframe.Low,
                                   dataframe.Close,
                                   timeperiod=14)

    # Add APO
    dataframe["APO"] = talib.APO(dataframe.Close,
                                 fastperiod=12,
                                 slowperiod=26,
                                 matype=0)

    # Add AROON
    dataframe["aroondown"], dataframe["aroonup"] = talib.AROON(dataframe.High,
                                                               dataframe.Low,
                                                               timeperiod=14)

    # Add AROONOSC
    dataframe["AROONOSC"] = talib.AROONOSC(dataframe.High,
                                           dataframe.Low,
                                           timeperiod=14)

    # Add BOP
    dataframe["BOP"] = talib.BOP(dataframe.Open, dataframe.High, dataframe.Low,
                                 dataframe.Close)

    # Add CCI
    dataframe["CCI"] = talib.CCI(dataframe.High,
                                 dataframe.Low,
                                 dataframe.Close,
                                 timeperiod=14)

    # Add CMO
    dataframe["CMO"] = talib.CMO(dataframe.Close, timeperiod=14)

    # Add DX
    dataframe["DX"] = talib.DX(dataframe.High,
                               dataframe.Low,
                               dataframe.Close,
                               timeperiod=14)

    # Add MACD : buy and sell signals
    dataframe['MACD'], dataframe['MACDSIGNAL'], dataframe[
        'MACDHIST'] = talib.MACD(dataframe.Close,
                                 fastperiod=12,
                                 slowperiod=26,
                                 signalperiod=9)

    # Add macdMACDEXT
    dataframe["macdMACDEXT"], dataframe["macdsignalMACDEXT"], dataframe[
        "macdhistMACDEXT"] = talib.MACDEXT(dataframe.Close,
                                           fastperiod=12,
                                           fastmatype=0,
                                           slowperiod=26,
                                           slowmatype=0,
                                           signalperiod=9,
                                           signalmatype=0)

    # Add macdMACDFIX
    dataframe["macdMACDFIX"], dataframe["macdsignalMACDFIX"], dataframe[
        "macdhistMACDFIX"] = talib.MACDFIX(dataframe.Close, signalperiod=9)

    # Add MFI
    dataframe["MFI"] = talib.MFI(dataframe.High,
                                 dataframe.Low,
                                 dataframe.Close,
                                 dataframe.Volume,
                                 timeperiod=14)

    # Add MINUS_DI
    dataframe["MINUS_DI"] = talib.MINUS_DI(dataframe.High,
                                           dataframe.Low,
                                           dataframe.Close,
                                           timeperiod=14)

    # Add MINUS_DM
    dataframe["MINUS_DM"] = talib.MINUS_DM(dataframe.High,
                                           dataframe.Low,
                                           timeperiod=14)

    # Add MOM
    dataframe["MOM"] = talib.MOM(dataframe.Close, timeperiod=10)

    # Add PLUS_DI
    dataframe["PLUS_DI"] = talib.PLUS_DI(dataframe.High,
                                         dataframe.Low,
                                         dataframe.Close,
                                         timeperiod=14)

    # Add PLUS_DM
    dataframe["PLUS_DM"] = talib.PLUS_DM(dataframe.High,
                                         dataframe.Low,
                                         timeperiod=14)

    # Add PPO
    dataframe["PPO"] = talib.PPO(dataframe.Close,
                                 fastperiod=12,
                                 slowperiod=26,
                                 matype=0)

    # Add ROC
    dataframe["ROC"] = talib.ROC(dataframe.Close, timeperiod=10)

    # Add ROCP
    dataframe["ROCP"] = talib.ROCP(dataframe.Close, timeperiod=10)

    # Add ROCR
    dataframe["ROCR"] = talib.ROCR(dataframe.Close, timeperiod=10)

    # Add ROCR100
    dataframe["ROCR100"] = talib.ROCR100(dataframe.Close, timeperiod=10)

    # Add RSI : information on over buying and over selling
    dataframe['RSI'] = talib.RSI(dataframe.Close, timeperiod=14)

    # Add Stochastic
    dataframe['slowk'], dataframe['slowd'] = talib.STOCH(dataframe.High,
                                                         dataframe.Low,
                                                         dataframe.Close,
                                                         fastk_period=5,
                                                         slowk_period=3,
                                                         slowk_matype=0,
                                                         slowd_period=3,
                                                         slowd_matype=0)

    # Add fastkSTOCHF
    dataframe["fastkSTOCHF"], dataframe["fastdSTOCHF"] = talib.STOCHF(
        dataframe.High,
        dataframe.Low,
        dataframe.Close,
        fastk_period=5,
        fastd_period=3,
        fastd_matype=0)

    # Add fastkSTOCHRSI
    dataframe["fastkSTOCHRSI"], dataframe["fastdSTOCHRSI"] = talib.STOCHRSI(
        dataframe.Close,
        timeperiod=14,
        fastk_period=5,
        fastd_period=3,
        fastd_matype=0)

    # Add TRIX
    dataframe["TRIX"] = talib.TRIX(dataframe.Close, timeperiod=30)

    # Add ULTOSC
    dataframe["ULTOSC"] = talib.ULTOSC(dataframe.High,
                                       dataframe.Low,
                                       dataframe.Close,
                                       timeperiod1=7,
                                       timeperiod2=14,
                                       timeperiod3=28)

    # Add WILLR : between 0 and -100 and measures overbought and oversold levels
    dataframe['WILLR'] = talib.WILLR(dataframe.High,
                                     dataframe.Low,
                                     dataframe.Close,
                                     timeperiod=14)

    # 3) Volume indicator function

    # Add AD
    dataframe['AD'] = talib.AD(dataframe.High, dataframe.Low, dataframe.Close,
                               dataframe.Volume)

    # Add ADOSC : the accumulation-distribution line of MACD
    dataframe['ADOSC'] = talib.ADOSC(dataframe.High,
                                     dataframe.Low,
                                     dataframe.Close,
                                     dataframe.Volume,
                                     fastperiod=3,
                                     slowperiod=10)

    # Add OBV : reflects the volume of transactions
    dataframe['OBV'] = talib.OBV(dataframe.Close, dataframe.Volume)

    # 4) Volatility Indicators

    # Add ATR : volatility indicator
    dataframe['ATR'] = talib.ATR(dataframe.High,
                                 dataframe.Low,
                                 dataframe.Close,
                                 timeperiod=14)

    # Add NATR : volatility indicator
    dataframe['NATR'] = talib.NATR(dataframe.High,
                                   dataframe.Low,
                                   dataframe.Close,
                                   timeperiod=14)

    # Add TRANGE : volatility indicator
    dataframe['TRANGE'] = talib.TRANGE(dataframe.High, dataframe.Low,
                                       dataframe.Close)

    # 5) Price Transform

    # Add AVGPRICE
    dataframe["AVGPRICE"] = talib.AVGPRICE(dataframe.Open, dataframe.High,
                                           dataframe.Low, dataframe.Close)

    # Add MEDPRICE
    dataframe["MEDPRICE"] = talib.MEDPRICE(dataframe.High, dataframe.Low)

    # Add TYPPRICE
    dataframe["TYPPRICE"] = talib.TYPPRICE(dataframe.High, dataframe.Low,
                                           dataframe.Close)

    # Add WCLPRICE
    dataframe["WCLPRICE"] = talib.WCLPRICE(dataframe.High, dataframe.Low,
                                           dataframe.Close)

    # 6) Cycle Indicators

    # Add HT_DCPERIOD
    dataframe["HT_DCPERIOD"] = talib.HT_DCPERIOD(dataframe.Close)

    # Add HT_DCPHASE
    dataframe["HT_DCPHASE"] = talib.HT_DCPHASE(dataframe.Close)

    # Add HT_PHASOR
    dataframe["inphase"], dataframe["quadrature"] = talib.HT_PHASOR(
        dataframe.Close)

    # Add HT_SINE
    dataframe["sine"], dataframe["leadsine"] = talib.HT_SINE(dataframe.Close)

    # Add HT_TRENDMODE
    dataframe["integer"] = talib.HT_TRENDMODE(dataframe.Close)

    # 7) Pattern Recognition

    dataframe["CDL2CROWS"] = talib.CDL2CROWS(dataframe.Open, dataframe.High,
                                             dataframe.Low, dataframe.Close)

    dataframe["CDL3BLACKCROWS"] = talib.CDL3BLACKCROWS(dataframe.Open,
                                                       dataframe.High,
                                                       dataframe.Low,
                                                       dataframe.Close)

    dataframe["CDL3INSIDE"] = talib.CDL3INSIDE(dataframe.Open, dataframe.High,
                                               dataframe.Low, dataframe.Close)

    dataframe["CDL3LINESTRIKE"] = talib.CDL3LINESTRIKE(dataframe.Open,
                                                       dataframe.High,
                                                       dataframe.Low,
                                                       dataframe.Close)

    dataframe["CDL3OUTSIDE"] = talib.CDL3OUTSIDE(dataframe.Open,
                                                 dataframe.High, dataframe.Low,
                                                 dataframe.Close)

    dataframe["CDL3STARSINSOUTH"] = talib.CDL3STARSINSOUTH(
        dataframe.Open, dataframe.High, dataframe.Low, dataframe.Close)

    dataframe["CDL3WHITESOLDIERS"] = talib.CDL3WHITESOLDIERS(
        dataframe.Open, dataframe.High, dataframe.Low, dataframe.Close)

    dataframe["CDLABANDONEDBABY"] = talib.CDLABANDONEDBABY(dataframe.Open,
                                                           dataframe.High,
                                                           dataframe.Low,
                                                           dataframe.Close,
                                                           penetration=0)

    dataframe["CDLADVANCEBLOCK"] = talib.CDLADVANCEBLOCK(
        dataframe.Open, dataframe.High, dataframe.Low, dataframe.Close)

    dataframe["CDLBELTHOLD"] = talib.CDLBELTHOLD(dataframe.Open,
                                                 dataframe.High, dataframe.Low,
                                                 dataframe.Close)

    dataframe["CDLBREAKAWAY"] = talib.CDLBREAKAWAY(dataframe.Open,
                                                   dataframe.High,
                                                   dataframe.Low,
                                                   dataframe.Close)

    dataframe["CDLCLOSINGMARUBOZU"] = talib.CDLCLOSINGMARUBOZU(
        dataframe.Open, dataframe.High, dataframe.Low, dataframe.Close)

    dataframe["CDLCONCEALBABYSWALL"] = talib.CDLCONCEALBABYSWALL(
        dataframe.Open, dataframe.High, dataframe.Low, dataframe.Close)

    dataframe["CDLCOUNTERATTACK"] = talib.CDLCOUNTERATTACK(
        dataframe.Open, dataframe.High, dataframe.Low, dataframe.Close)

    dataframe["CDLDARKCLOUDCOVER"] = talib.CDLDARKCLOUDCOVER(dataframe.Open,
                                                             dataframe.High,
                                                             dataframe.Low,
                                                             dataframe.Close,
                                                             penetration=0)

    dataframe["CDLDOJI"] = talib.CDLDOJI(dataframe.Open, dataframe.High,
                                         dataframe.Low, dataframe.Close)

    dataframe["CDLDOJISTAR"] = talib.CDLDOJISTAR(dataframe.Open,
                                                 dataframe.High, dataframe.Low,
                                                 dataframe.Close)

    dataframe["CDLDRAGONFLYDOJI"] = talib.CDLDRAGONFLYDOJI(
        dataframe.Open, dataframe.High, dataframe.Low, dataframe.Close)

    dataframe["CDLENGULFING"] = talib.CDLENGULFING(dataframe.Open,
                                                   dataframe.High,
                                                   dataframe.Low,
                                                   dataframe.Close)

    dataframe["CDLEVENINGDOJISTAR"] = talib.CDLEVENINGDOJISTAR(dataframe.Open,
                                                               dataframe.High,
                                                               dataframe.Low,
                                                               dataframe.Close,
                                                               penetration=0)

    dataframe["CDLEVENINGSTAR"] = talib.CDLEVENINGSTAR(dataframe.Open,
                                                       dataframe.High,
                                                       dataframe.Low,
                                                       dataframe.Close,
                                                       penetration=0)

    dataframe["CDLGAPSIDESIDEWHITE"] = talib.CDLGAPSIDESIDEWHITE(
        dataframe.Open, dataframe.High, dataframe.Low, dataframe.Close)

    dataframe["CDLGRAVESTONEDOJI"] = talib.CDLGRAVESTONEDOJI(
        dataframe.Open, dataframe.High, dataframe.Low, dataframe.Close)

    dataframe["CDLHAMMER"] = talib.CDLHAMMER(dataframe.Open, dataframe.High,
                                             dataframe.Low, dataframe.Close)

    dataframe["CDLHANGINGMAN"] = talib.CDLHANGINGMAN(dataframe.Open,
                                                     dataframe.High,
                                                     dataframe.Low,
                                                     dataframe.Close)

    dataframe["CDLHARAMI"] = talib.CDLHARAMI(dataframe.Open, dataframe.High,
                                             dataframe.Low, dataframe.Close)

    dataframe["CDLHARAMICROSS"] = talib.CDLHARAMICROSS(dataframe.Open,
                                                       dataframe.High,
                                                       dataframe.Low,
                                                       dataframe.Close)

    dataframe["CDLHIGHWAVE"] = talib.CDLHIGHWAVE(dataframe.Open,
                                                 dataframe.High, dataframe.Low,
                                                 dataframe.Close)

    dataframe["CDLHIKKAKE"] = talib.CDLHIKKAKE(dataframe.Open, dataframe.High,
                                               dataframe.Low, dataframe.Close)

    dataframe["CDLHIKKAKEMOD"] = talib.CDLHIKKAKEMOD(dataframe.Open,
                                                     dataframe.High,
                                                     dataframe.Low,
                                                     dataframe.Close)

    dataframe["CDLHOMINGPIGEON"] = talib.CDLHOMINGPIGEON(
        dataframe.Open, dataframe.High, dataframe.Low, dataframe.Close)

    dataframe["CDLIDENTICAL3CROWS"] = talib.CDLIDENTICAL3CROWS(
        dataframe.Open, dataframe.High, dataframe.Low, dataframe.Close)

    dataframe["CDLINNECK"] = talib.CDLINNECK(dataframe.Open, dataframe.High,
                                             dataframe.Low, dataframe.Close)

    dataframe["CDLINVERTEDHAMMER"] = talib.CDLINVERTEDHAMMER(
        dataframe.Open, dataframe.High, dataframe.Low, dataframe.Close)

    dataframe["CDLKICKING"] = talib.CDLKICKING(dataframe.Open, dataframe.High,
                                               dataframe.Low, dataframe.Close)

    dataframe["CDLKICKINGBYLENGTH"] = talib.CDLKICKINGBYLENGTH(
        dataframe.Open, dataframe.High, dataframe.Low, dataframe.Close)

    dataframe["CDLLADDERBOTTOM"] = talib.CDLLADDERBOTTOM(
        dataframe.Open, dataframe.High, dataframe.Low, dataframe.Close)

    dataframe["CDLLONGLEGGEDDOJI"] = talib.CDLLONGLEGGEDDOJI(
        dataframe.Open, dataframe.High, dataframe.Low, dataframe.Close)

    dataframe["CDLLONGLINE"] = talib.CDLLONGLINE(dataframe.Open,
                                                 dataframe.High, dataframe.Low,
                                                 dataframe.Close)

    dataframe["CDLMARUBOZU"] = talib.CDLMARUBOZU(dataframe.Open,
                                                 dataframe.High, dataframe.Low,
                                                 dataframe.Close)

    dataframe["CDLMATCHINGLOW"] = talib.CDLMATCHINGLOW(dataframe.Open,
                                                       dataframe.High,
                                                       dataframe.Low,
                                                       dataframe.Close)

    dataframe["CDLMATHOLD"] = talib.CDLMATHOLD(dataframe.Open,
                                               dataframe.High,
                                               dataframe.Low,
                                               dataframe.Close,
                                               penetration=0)

    dataframe["CDLMORNINGDOJISTAR"] = talib.CDLMORNINGDOJISTAR(dataframe.Open,
                                                               dataframe.High,
                                                               dataframe.Low,
                                                               dataframe.Close,
                                                               penetration=0)

    dataframe["CDLMORNINGSTAR"] = talib.CDLMORNINGSTAR(dataframe.Open,
                                                       dataframe.High,
                                                       dataframe.Low,
                                                       dataframe.Close,
                                                       penetration=0)

    dataframe["CDLONNECK"] = talib.CDLONNECK(dataframe.Open, dataframe.High,
                                             dataframe.Low, dataframe.Close)

    dataframe["CDLPIERCING"] = talib.CDLPIERCING(dataframe.Open,
                                                 dataframe.High, dataframe.Low,
                                                 dataframe.Close)

    dataframe["CDLRICKSHAWMAN"] = talib.CDLRICKSHAWMAN(dataframe.Open,
                                                       dataframe.High,
                                                       dataframe.Low,
                                                       dataframe.Close)

    dataframe["CDLRISEFALL3METHODS"] = talib.CDLRISEFALL3METHODS(
        dataframe.Open, dataframe.High, dataframe.Low, dataframe.Close)

    dataframe["CDLSEPARATINGLINES"] = talib.CDLSEPARATINGLINES(
        dataframe.Open, dataframe.High, dataframe.Low, dataframe.Close)

    dataframe["CDLSHOOTINGSTAR"] = talib.CDLSHOOTINGSTAR(
        dataframe.Open, dataframe.High, dataframe.Low, dataframe.Close)

    dataframe["CDLSHORTLINE"] = talib.CDLSHORTLINE(dataframe.Open,
                                                   dataframe.High,
                                                   dataframe.Low,
                                                   dataframe.Close)

    dataframe["CDLSPINNINGTOP"] = talib.CDLSPINNINGTOP(dataframe.Open,
                                                       dataframe.High,
                                                       dataframe.Low,
                                                       dataframe.Close)

    dataframe["CDLSTALLEDPATTERN"] = talib.CDLSTALLEDPATTERN(
        dataframe.Open, dataframe.High, dataframe.Low, dataframe.Close)

    dataframe["CDLSTICKSANDWICH"] = talib.CDLSTICKSANDWICH(
        dataframe.Open, dataframe.High, dataframe.Low, dataframe.Close)

    dataframe["CDLTAKURI"] = talib.CDLTAKURI(dataframe.Open, dataframe.High,
                                             dataframe.Low, dataframe.Close)

    dataframe["CDLTASUKIGAP"] = talib.CDLTASUKIGAP(dataframe.Open,
                                                   dataframe.High,
                                                   dataframe.Low,
                                                   dataframe.Close)

    dataframe["CDLTHRUSTING"] = talib.CDLTHRUSTING(dataframe.Open,
                                                   dataframe.High,
                                                   dataframe.Low,
                                                   dataframe.Close)

    dataframe["CDLTRISTAR"] = talib.CDLTRISTAR(dataframe.Open, dataframe.High,
                                               dataframe.Low, dataframe.Close)

    dataframe["CDLUNIQUE3RIVER"] = talib.CDLUNIQUE3RIVER(
        dataframe.Open, dataframe.High, dataframe.Low, dataframe.Close)

    dataframe["CDLUPSIDEGAP2CROWS"] = talib.CDLUPSIDEGAP2CROWS(
        dataframe.Open, dataframe.High, dataframe.Low, dataframe.Close)

    dataframe["CDLXSIDEGAP3METHODS"] = talib.CDLXSIDEGAP3METHODS(
        dataframe.Open, dataframe.High, dataframe.Low, dataframe.Close)

    return dataframe
