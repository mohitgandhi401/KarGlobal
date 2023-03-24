# KarGlobal Interview Web application and Deployment

1) We are using Flask Framework in python to build the web application
2) The Home page accepts three numbers and on pressing submit we get all the combinations of the numbers
3) I have created a dockefile to containerise the application
4) Pyopenssl is used to TLS 
5) Github actions is used for CI. It is responsible for building and pushing the image to dockerhub
6) I have also included kubernetes deployment in the repository which can be used to deploy the web application in any specific cluster. 
It can be done using kubectl (manually) or using CD tools like ArgoCD to do it.
7) WAF can be used to secure it further.
8) Screenshots are added to results folder.