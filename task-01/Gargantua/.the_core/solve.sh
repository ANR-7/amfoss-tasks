echo "Enter string" 
read -r string
echo "$string" | openssl enc -base64 -d -A 
