def arithmetic_arranger(problems:list, ans=False)->str:
  l1=l2=l3=l4='' #four lines of answers
  if len(problems)>5: return 'Error: Too many problems.'
  for ques in problems:
    if not ('+' in ques or '-' in ques) or ('*' in ques or '/' in ques):
      return "Error: Operator must be '+' or '-'."

    pm='+' if '+' in ques else '-' #plus oder minus
    nr1, nr2=ques.split(pm)
    nr1, nr2=nr1.strip(), nr2.strip()
    ll=max(len(nr1), len(nr2)) # length of longer number
    for nr_lp in [nr1, nr2]:
      if not nr_lp.isdigit(): return "Error: Numbers must only contain digits."
    if ll>4: return "Error: Numbers cannot be more than four digits."

    l1+=' '*(ll-len(nr1)+2+4) + nr1 #add 4 spaces also to the to the first number and remove them by the end
    l2+=' '*4 + pm + ' '*(ll-len(nr2)+1) + nr2
    l3+=' '*4 + '-'*(ll+2)
    ans_lp=int(nr1)+int(nr2) if pm=='+' else int(nr1)-int(nr2)
    l4+=' '*(ll-len(str(ans_lp))+2+4) + str(ans_lp)

  l1=l1[4:]+'\n'
  l2=l2[4:]+'\n'
  l3=l3[4:]
  l4='\n'+l4[4:]

  arranged_problems=l1+l2+l3
  if ans: arranged_problems+=l4
  return arranged_problems