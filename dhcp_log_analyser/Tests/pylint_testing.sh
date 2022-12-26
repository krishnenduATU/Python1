#!/bin/bash
############################
# Script  : pylint_testing.sh
# Author  : Krishnendu
# Purpose : To review python script using pylint code analyser
# Usage   : ./pylint_testing.sh
# Version : 06-Nov-2022
# Tested  : Ubuntu 22.04.1 LTS with Python version 3.10.6 
# Notes   : Pylint is a static code analysis tool for the Python programming language.
# Prerequisites : python3, python3-pip, pylint
###########################

# To print script usage
function help() {
	echo "Usage: pylint_testing.py"
	echo "User can provide directory or python file for testing"
	echo "quick_test : To print only code ratings"
	echo "smart_test : To print details code review"
}
# To perform a quick test, only code rating is printed in output
function quick_test() {
	# Check if directory or file
	if [ -d "$input_path" ]; then
		# Finds all the file in the directory provided
		for file in $(find $input_path -name "*.py"); do
       			echo -ne "CODE : $file \t ";
			# To print last line from pylint report with rating
       			pylint $file | tail -2 | awk '/Your code/ {print "RATING : " $7}'; 
		done
	else
            	 pylint $input_path | tail -2 | awk '/Your code/ {print "RATING : " $7}'
	fi
}
# To perform detailed analysis of the code and print detailed report of the code
function smart_test() {
        if [ -d "$input_path" ]; then
                for file in $(find $input_path -name "*.py"); do
                	echo -ne "CODE : $file \t ";
               		pylint $file;
        	done
	else
                pylint $input_path
        fi

}

read -erp "Enter directory/file name to test code : " input_path
read -erp "Would you like perform quick or smart test : " input_test

case $input_test in 
	smart|s|S)
		echo "Performing smart/detailed test, please wait.."
		smart_test
	  ;;
	quick|q|Q)
		echo "Performing quick test, please wait.."
		quick_test
	  ;;
	*)
          echo "Invalid argument !!"
	  help
	  ;;
esac
