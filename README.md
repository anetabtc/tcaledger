# tcaledger
PVE with tcaledger app for payments and simulation of payment requests.

This application, made using the Django framework, has the functionality of receiving and processing post and get requests, to ensure that orders are accepted and placed in the database, as well as to verify the success of the payment process.

To implement the last point, the cardano-wallet REST API is used, with the help of which it is possible to obtain up-to-date information regarding the balance on the preferred local wallet and reconcile changes in the current amount to approve the success of the payment made.

This repository is an open-source payment API that allows individuals and merchants to accept Cardano (ADA) on thier websites. We integrated this API on a Wix website, however it is compatible with most all websites. 

To keep up with the Aneta team, you can follow us at @anetabtc on Twitter. 
