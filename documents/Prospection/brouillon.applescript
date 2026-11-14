on run argv
	set {dest, sujet, htmlPath, pdfPath} to argv
	set corps to read (POSIX file htmlPath) as «class utf8»
	tell application "Mail"
		set m to make new outgoing message with properties {subject:sujet, visible:false}
		set sender of m to "Antoine Pittilloni <antoine.pittilloni@gmail.com>"
		set html content of m to corps
		tell m
			make new to recipient at end of to recipients with properties {address:dest}
			make new attachment with properties {file name:(POSIX file pdfPath) as alias} at after last paragraph of content
		end tell
		delay 2
		save m
		delay 1
		close m saving yes
	end tell
	return "ok " & dest
end run
