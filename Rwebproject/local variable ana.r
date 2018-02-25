library(astsa)
library(forecast)
library(chron)
library(psych)
library(matrixStats)

#data processing
coin=read.csv2("coin_1.csv",sep = ",",dec=".",header =TRUE,stringsAsFactors=F, na.strings="unknown")
as.numeric(coin[,-1])
time=as.POSIXct(coin[,1],origin="1970-01-01",tz="GMT")

close_off_high=2*(coin[,3]-coin[,4])/(coin[,4]-coin[,5])+1
volatility=(coin[,4]-coin[,5])/coin[,2]

normal_coin=coin
normal_coin=normal_coin[,-1]
for(i in 1:40 ){
  #i=1
  sd=colSds(as.matrix(coin[10*(i-1)+1:10,-1]))
  for (j in 1: 10){
    normal_coin[10*(i-1)+j,]=coin[10*(i-1)+j,-1]-coin[10*(i-1)+1,-1]
    normal_coin[10*(i-1)+j,]=normal_coin[10*(i-1)+j,-1]/sd
  }
   # normal_coin[10*(i-1)+1:10*(i-1)+10,]=normal_coin[10*(i-1)+1:10*(i-1)+10,]))/sd
}

coin_train=cbind(time,normal_coin,close_off_high,volatility)
#View(coin_train)
write.csv(coin_train,"coin_train.csv",row.names = FALSE)
#setNames(coin_train[,1]="time")
# time(coin[,1])
# time_series=ts(coin[,2])
# summary(lm(time_series~time))
# ts.plot(time_series)
# ts.plot(log(time_series))
# acf2(diff(time_series))
# arima=auto.arima(coin[,2])
# summary(arima)
# factors=arima$arma
# sarima.for(coin[,2],24,p=factors[1],d=factors[3],q=factors[2],P=factors[6],D=factors[5],Q=factors[7],S=factors[5])

#plot(time_series)
