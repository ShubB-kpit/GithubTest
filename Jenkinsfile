pipeline {
    agent any
     
    stages {
        stage('Ok') {
            steps {
                echo "Ok"
            }
        }
    }
    post {
        always {
            emailext body: 'testing',subject: 'testing', to: 'shubham.bawankar@kpit.com'
        }
    }
}
