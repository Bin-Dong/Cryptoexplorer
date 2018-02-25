#
# This is the server logic of a Shiny web application. You can run the 
# application by clicking 'Run App' above.
#
# Find out more about building applications with Shiny here:
# 
#    http://shiny.rstudio.com/
#

library(shiny)
library(astsa)
library(forecast)
# Define server logic required to draw a histogram
shinyServer(function(input, output) {
   
  output$distPlot <- renderPlot({
    
    # generate bins based on input$bins from ui.R
    
    x    <- faithful[, 2] 
    bins <- seq(min(x), max(x), length.out = input$bins + 1)
    arima=auto.arima(UnempRate)
    factors=arima$arma
    
    sarima.for(UnempRate,24, 5,  1,  5,  1, 0,  0, 12)
    sarima.for(UnempRate,24,p=factors[1],d=factors[3],q=factors[2],P=factors[6],D=factors[5],Q=factors[7],S=factors[5])
    # draw the histogram with the specified number of bins
    #hist(x, breaks = bins, col = 'darkgray', border = 'white')
    
  })
  
})
