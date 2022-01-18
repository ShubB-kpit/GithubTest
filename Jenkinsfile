pipeline {
    agent any
    stages {
        stage('Welcome Step') {
            steps { 
                echo 'Welcome to the LambdaTest'
            }
        }
        stage('check if py file exists'){
            steps {
                
                script {
                    if(fileExists("./branch2_1/test_pySh.py")) {
                        echo 'py file exists'
                        var1 = bat(script:'python ./branch2_1/test_pySh.py', returnStdout: true).trim()
                        echo "${var1}"
                        mail to:'shubham.bawankar@kpit.com',
                        subject:'test email1',
                        body:var1
                        
                        
                    }
                    else {
                        echo '404: file not exists'
                    }
                }
                
            }
            
        }
    }
}
