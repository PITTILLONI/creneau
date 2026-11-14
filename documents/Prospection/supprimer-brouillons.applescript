on run argv
	set n to 0
	tell application "Mail"
		repeat with mb in mailboxes of account "Google Perso"
			if name of mb is "Brouillons" then
				repeat with sujet in argv
					set L to (messages of mb whose subject is (sujet as text))
					repeat with m in L
						delete m
						set n to n + 1
					end repeat
				end repeat
			end if
		end repeat
	end tell
	return n
end run
