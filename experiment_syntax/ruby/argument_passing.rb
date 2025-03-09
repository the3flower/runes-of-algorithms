# Positional and Keyword Arguments

def send_message(recipient, content:, urgency: "normal", sender: "System")
    puts "[#{urgency.capitalize}] From: #{sender} - To: #{recipient}: #{content}"
end

send_message("Bob", content: "Your order is ready", urgency: "high", sender: "Shop")
# Output: [High] From: Shop - To: Bob: Your order is ready

# Keyword argument can be any position
send_message("Bob", sender: "Shop", urgency: "high", content: "Your order is ready")
# Output: [High] From: Shop - To: Bob: Your order is ready

# Pass using hash
options = { content: "See you tomorrow", urgency: "low", sender: "Teacher" }
send_message("David", **options)
# Output: [Low] From: Teacher - To: David: See you tomorrow
