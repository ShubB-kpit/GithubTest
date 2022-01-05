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
                when {
                    expression {
                        File("/branch2_1/pyTest1.py").exists()
                    }
                }
                echo 'py file exists'
            }
            steps {
                when {
                    expression {
                        !File("/branch2_1/pyTest1.py").exists()
                    }
                }
                echo '404: file not exists'
            }
        }
    }
}
