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
                        bat '''
                        python branch2_1/test_pySh.py > tt
                        set /p var1 = <tt
                        DEL tt
                        '''
                        echo "${var1}"
                    }
                    else {
                        echo '404: file not exists'
                    }
                }
                
            }
            
        }
    }
}
