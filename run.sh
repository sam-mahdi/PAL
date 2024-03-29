if [ $1 == "no_photo" ]
    then 
        cd PAL
        python3 PAL.py no_photo
else
    if [ ! -d "PAL_virtual_environment" ]
        then 
            echo "creating virtual environment"
            python3 -m venv PAL_virtual_environment
            source PAL_virtual_environment/bin/activate
            echo "install requirements"
            pip install --upgrade pip
            pip install --upgrade setuptools
            pip install -r requirements.txt
            cp -r PAL PAL_virtual_environment
            cd PAL_virtual_environment
            cd PAL
            python3 PAL.py blob
    else
         source PAL_virtual_environment/bin/activate
         cd PAL_virtual_environment
         cd PAL
         python3 PAL.py blob
    fi     
fi
