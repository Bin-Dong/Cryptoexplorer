library(astsa)
library(forecast)
library(chron)
library(psych)
library(matrixStats)
library(kerasR)
library(reticulate)
library(vars)



#data processing
 coin=read.csv2("coin_1.csv",sep = ",",dec=".",header =TRUE,stringsAsFactors=F, na.strings="unknown")
 as.numeric(coin[,-1])
 time=as.POSIXct(coin[,1],origin="1970-01-01",tz="GMT")
 

 
 ##data processing for machine learning input
# close_off_high=2*(coin[,3]-coin[,4])/(coin[,4]-coin[,5])+1
# volatility=(coin[,4]-coin[,5])/coin[,2]
# 
# normal_coin=coin
# normal_coin=normal_coin[,-1]
# 
# for(i in 1:40 ){
#   #i=1
#   sd=colSds(as.matrix(coin[10*(i-1)+1:10,-1]))
#   for (j in 1: 10){
#     normal_coin[10*(i-1)+j,]=coin[10*(i-1)+j,-1]-coin[10*(i-1)+1,-1]
#     normal_coin[10*(i-1)+j,]=normal_coin[10*(i-1)+j,]/sd
#   }
# }
# 
# coin_train=cbind(time,normal_coin,close_off_high,volatility)
# #View(coin_train)
# write.csv(coin_train,"coin_train.csv",row.names = FALSE)
# View(coin)
# 
# 
# #LSTM analysis
# mod<-Sequential()

 
 
 #basic VAR model processing
 time_series=ts(coin[,2])
 
 var.result=VAR(coin[,1:2],p=1,type="trend")
 pred=predict(var.result, n.ahead = 8, ci = 0.95)
 ts.plot(pred$endog[,2]) 
 time=as.POSIXct(pred$endog[,1],origin="1970-01-01",tz="GMT")
 # write.csv(coin_train,"coin_train.csv",row.names = FALSE)
 
#colSds(as.matrix(coin[391:400,-1]))
#setNames(coin_train[,1]="time")
# time(coin[,1])
# summary(lm(time_series~time))
# ts.plot(time_series)
# ts.plot(log(time_series))
# acf2(diff(time_series))


 #arima=auto.arima(coin[,2])
 #acf2(time_series)
# summary(arima)
# factors=arima$arma

 # manually analysis
  # reg=lm(coin[,2]~time)
 # ts.plot(reg$residual)
 # acf2(reg$residuals)
  sarima.for(coin[,2],24,1,1,0,1,0,1,30)
 # auto.arima(reg$residuals)
#plot(time_series)
