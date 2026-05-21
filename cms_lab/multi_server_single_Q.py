; Customer
        GENERATE    18,6        ; Customers arrive every 18 +/- 6 minutes
        QUEUE       Line        ; Enter the line (queue)
        
; The number of barbers (servers) is 3
; The system will seize any available barber from the pool
        SEIZE       Barber1     ; Capture the first barber (server)
        SEIZE       Barber2     ; Capture the second barber (server)
        SEIZE       Barber3     ; Capture the third barber (server)
        
        DEPART      Line        ; Leave the line after being served
        ADVANCE     16,4        ; Use the barber (service time) 16 +/- 4 minutes
        RELEASE     Barber1     ; Free the first barber (server)
        RELEASE     Barber2     ; Free the second barber (server)
        RELEASE     Barber3     ; Free the third barber (server)
        TERMINATE               ; Leave the shop after service

; Timer
        GENERATE    480         ; Timer arrives after 480 minutes (8 hours)
        TERMINATE   1           ; Shut off the run after 480 minutes

; Control
        START       1           ; Start the run
