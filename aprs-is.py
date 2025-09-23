import aprslib
import logging

logging.basicConfig(level=logging.INFO)

# Define a callback function to handle each received packet
def handle_packet(packet):
    if packet.get('from') == target_callsign:
        print(packet)

# target callsign
target_callsign = 'W1AW'

# Replace 'N0CALL' with your own amateur radio callsign, only if sending
user_callsign = 'N0CALL'

try:
    # get passcode from my callsign
    #pcode = aprslib.passcode(user_callsign)
    
    # create object
    ais = aprslib.IS(user_callsign)

    # Establish the connection to the APRS-IS server
    print("Connecting...")
    ais.connect()
    print(f"Searching for {target_callsign}")
    
    # Start consuming packets. This runs indefinitely.
    # The `consumer` method will automatically parse each packet.
    ais.consumer(handle_packet)
except aprslib.ParseError as e:
    print(f"Parse error: {e}")
except Exception as e:
    print(f"Error: {e}")


