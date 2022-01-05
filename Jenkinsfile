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
                step {
                    when {
                        expression {
                            File("/path-to-file").exists()
                        }
                    }
                    echo 'py file exists'
                }
                step {
                    when {
                        expression {
                            !File("/path-to-file").exists()
                        }
                    }
                    echo '404: file not exists'
                }
            }
        }
    }
}
