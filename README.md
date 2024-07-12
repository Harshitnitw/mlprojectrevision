# end to end ml project revision

## rename github codespace to avoid confusion later

## set backgroud dark by using the following:
You can open the settings.json file with the Preferences: Open User Settings (JSON) command in the Command Palette (Ctrl+Shift+P).
```
{
	"workbench.colorCustomizations": {
        "editor.background": "#000000",
        "activityBar.background": "#000000"
	}
}
```

## ctrl + , -> setting opens: search editor font size, make 14 (increase 4 points) or ctrl + shift + p, editor font size, click setting button and make shortcut for increasing text size

## if github repository not linked to codespace then in codespace terminal write:
```
git init
git add README.md
git commit -m "first commit"
git status
git branch -M main
git remote add origin https://github.com/Harshitnitw/mlproject.git # change 'Harshitnitw/mlproject.git'
git remote -v
# set/change 'git global config' by the following code if not configured:
git config --global user.name "John Doe"
git config --global user.email "john@example.com"
# if want to check the current email config then:
git config --global user.email
git push -u origin main
```

## add .gitignore file in github.com before installing conda environment so that  venv doesn't get pushed upon git push

## create conda environment by using following commands in terminal:
`conda create -p venv python==3.8 -y`

`conda init`

(stop current codespace and reopen)

## to make conda environment as default follow this solution given by chatgpt: 
https://chatgpt.com/share/8fbe75ed-9480-48ac-a8cc-36ea8f5286d1

if using github codespace and named conda environment as venv then the code to put is:

1. use `nano ~/.bashrc` in terminal to open editor
2. paste the following code at last after replacing [GITHUB CODESPACE NAME]:

```
__conda_setup="$('/opt/conda/bin/conda' 'shell.bash' 'hook' 2> /dev/null)"
if [ $? -eq 0 ]; then
    eval "$__conda_setup"
else
    if [ -f "/opt/conda/etc/profile.d/conda.sh" ]; then
        . "/opt/conda/etc/profile.d/conda.sh"
    else
        export PATH="/opt/conda/bin:$PATH"
    fi
fi
unset __conda_setup

conda activate /workspace/[GITHUB CODESPACE NAME]/venv
```

3. reload shell configuration by using `source ~/.bashrc` in terminal

## While using jupyter notebook (ipynb file) in codespace, select kernel -> install -> python environments -> venv enviroment (conda python 3.8.0 installed in this example), would install pypy kernel

## Running cells with 'venv (Python 3.8.5)' requires the ipykernel package. Run the following command in terminal to install 'ipykernel' into the Python environment. 
'conda install -p /workspaces/mlprojectrevision/venv ipykernel --update-deps --force-reinstall -y'

## If jupiter notebook slow or buggy then open in google colab, download the completed  file and upload in codespace