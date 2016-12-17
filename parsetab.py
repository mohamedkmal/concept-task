
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.8'

_lr_method = 'LALR'

_lr_signature = '9680E4C589859855CB0FBCD3A99FE814'
    
_lr_action_items = {'DIVID':([1,4,5,7,21,],[-18,-19,-20,-17,28,]),'CLOSEPRACS':([1,4,5,7,21,22,23,24,27,34,35,36,37,38,39,],[-18,-19,-20,-17,-11,32,-16,-14,34,-12,-10,-7,-8,-9,-15,]),'PLUS':([1,4,5,7,21,],[-18,-19,-20,-17,29,]),'FLOAT':([0,8,10,16,18,19,20,28,29,30,31,33,],[5,5,5,5,5,5,5,5,5,5,5,5,]),'MULTIPLY':([1,4,5,7,21,],[-18,-19,-20,-17,31,]),'VAR':([0,8,10,16,18,19,20,28,29,30,31,33,],[7,7,12,7,7,12,7,7,7,7,7,7,]),'COMMA':([1,4,5,7,21,23,24,34,35,36,37,38,],[-18,-19,-20,-17,-11,-16,33,-12,-10,-7,-8,-9,]),'OPENPRACS':([12,16,18,20,28,29,30,31,33,],[16,20,20,20,20,20,20,20,20,]),'INT':([0,8,10,16,18,19,20,28,29,30,31,33,],[4,4,4,4,4,4,4,4,4,4,4,4,]),'EQUAL':([1,4,5,12,14,],[-18,-19,-20,-17,18,]),'MINUS':([1,4,5,7,21,],[-18,-19,-20,-17,30,]),'END':([13,19,26,],[17,-4,-3,]),'BEGIN':([1,4,5,7,9,],[-18,-19,-20,-17,10,]),'ASSIGN':([1,2,4,5,7,],[-18,8,-19,-20,-17,]),'$end':([3,6,17,],[0,-1,-2,]),'SEMICOLUMN':([1,4,5,7,11,15,21,25,32,34,35,36,37,38,],[-18,-19,-20,-17,-6,19,-11,-5,-13,-12,-10,-7,-8,-9,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'constant':([0,8,10,16,18,19,20,28,29,30,31,33,],[1,1,1,1,1,1,1,1,1,1,1,1,]),'var':([0,8,10,16,18,19,20,28,29,30,31,33,],[2,9,14,21,21,14,21,21,21,21,21,21,]),'parameterList':([16,33,],[22,39,]),'Start':([0,],[3,]),'functioncall':([10,19,],[11,11,]),'statement':([10,19,],[15,15,]),'parameter':([16,33,],[24,24,]),'foreach':([0,],[6,]),'expr':([16,18,20,28,29,30,31,33,],[23,25,27,35,36,37,38,23,]),'statementlist':([10,19,],[13,26,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> Start","S'",1,None,None,None),
  ('Start -> foreach','Start',1,'p_startforeach','parse.py',42),
  ('foreach -> var ASSIGN var BEGIN statementlist END','foreach',6,'p_foreach','parse.py',46),
  ('statementlist -> statement SEMICOLUMN statementlist','statementlist',3,'p_statementlist','parse.py',53),
  ('statementlist -> statement SEMICOLUMN','statementlist',2,'p_statementlist','parse.py',54),
  ('statement -> var EQUAL expr','statement',3,'p_statement','parse.py',62),
  ('statement -> functioncall','statement',1,'p_statement','parse.py',63),
  ('expr -> var PLUS expr','expr',3,'p_expr','parse.py',70),
  ('expr -> var MINUS expr','expr',3,'p_expr','parse.py',71),
  ('expr -> var MULTIPLY expr','expr',3,'p_expr','parse.py',72),
  ('expr -> var DIVID expr','expr',3,'p_expr','parse.py',73),
  ('expr -> var','expr',1,'p_expr','parse.py',74),
  ('expr -> OPENPRACS expr CLOSEPRACS','expr',3,'p_expr','parse.py',75),
  ('functioncall -> VAR OPENPRACS parameterList CLOSEPRACS','functioncall',4,'p_function','parse.py',82),
  ('parameterList -> parameter','parameterList',1,'p_parameterList','parse.py',90),
  ('parameterList -> parameter COMMA parameterList','parameterList',3,'p_parameterList','parse.py',91),
  ('parameter -> expr','parameter',1,'p_parameter','parse.py',98),
  ('var -> VAR','var',1,'p_var','parse.py',105),
  ('var -> constant','var',1,'p_var','parse.py',106),
  ('constant -> INT','constant',1,'p_constant','parse.py',113),
  ('constant -> FLOAT','constant',1,'p_constant','parse.py',114),
]
