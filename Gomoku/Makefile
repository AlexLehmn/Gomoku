##
## EPITECH PROJECT, 2020
## Makefile
## File description:
## makefile
##

## pyinstaller --onefile main.py

EXE_NAME = pbrain-gomoku-ai

ifeq ($(shell echo "check_quotes"),"check_quotes")
CP := copy .\main.py .\$(EXE_NAME)
CHMOD := icacls $(EXE_NAME) /grant "$($env:username):(F)"
RM := del $(EXE_NAME)
else
CP := cp -f ./main.py ./$(EXE_NAME)
CHMOD := chmod +x $(EXE_NAME)
RM := rm -f $(EXE_NAME)
endif

all:
	$(CP)
	$(CHMOD)

clean:
	$(RM)

fclean:	clean

re:	clean fclean all

.PHONY: all clean fclean re
