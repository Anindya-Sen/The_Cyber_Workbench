# A06 – Discover cryptographic implementation used offline


One cryptographic implementation used offline that I found really interesting is chip-based card payment. Using a debit or credit card at a shop is such a normal part of everyday life that it is easy to ignore how much security is actually built into it. After looking into it, I found that EMVCo, the organisation that manages the EMV standard originally named after Europay, Mastercard, and Visa, explains that chip-card payments use advanced cryptography to make transactions more secure. Instead of sending the same fixed information every time, the chip creates a one-time security code, also called a cryptogram, for each transaction. This means the card is proving that the payment is genuine in that specific moment, rather than simply repeating stored card details that could be copied and reused.

What makes the cryptography here important is that the one-time code is unique for each transaction, so it cannot just be captured and used again later in the same way as old magnetic-stripe data. In simple terms, when the card is inserted or tapped, the chip and payment terminal exchange information, and the chip generates a special secure code using cryptographic processing. The bank or card issuer can then check that this code is valid, which helps confirm that the card is real and the transaction has not been faked. This makes chip-card payment a strong example of offline cryptography because the security is happening during a physical in-store transaction, but it still depends on cryptographic protection working silently in the background.


### Reference link: https://www.aciworldwide.com/emv-payments-transactions
### *Evidences attached on this Github Repository sub-folder*
