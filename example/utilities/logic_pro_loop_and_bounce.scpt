FasdUAS 1.101.10   ��   ��    k             l     ��  ��    c ]set targetFolder to "/Users/mac/PycharmProjects/youtube_sleep_automation/staging_files/music"     � 	 	 � s e t   t a r g e t F o l d e r   t o   " / U s e r s / m a c / P y c h a r m P r o j e c t s / y o u t u b e _ s l e e p _ a u t o m a t i o n / s t a g i n g _ f i l e s / m u s i c "   
  
 l     ��  ��    p jset saveToFolder to "/Users/mac/PycharmProjects/youtube_sleep_automation/staging_files/10_hr_looped_music"     �   � s e t   s a v e T o F o l d e r   t o   " / U s e r s / m a c / P y c h a r m P r o j e c t s / y o u t u b e _ s l e e p _ a u t o m a t i o n / s t a g i n g _ f i l e s / 1 0 _ h r _ l o o p e d _ m u s i c "      l     ��������  ��  ��        l     ��  ��    = 7 Read environment variables for target and save folders     �   n   R e a d   e n v i r o n m e n t   v a r i a b l e s   f o r   t a r g e t   a n d   s a v e   f o l d e r s      l     ����  r         I    �� ��
�� .sysoexecTEXT���     TEXT  m        �   $ e c h o   $ t a r g e t F o l d e r��    o      ���� 0 targetfolder targetFolder��  ��        l     ����   r     ! " ! I   �� #��
�� .sysoexecTEXT���     TEXT # m    	 $ $ � % % $ e c h o   $ s a v e T o F o l d e r��   " o      ���� 0 savetofolder saveToFolder��  ��     & ' & l     ��������  ��  ��   '  ( ) ( l     ��������  ��  ��   )  * + * l    ,���� , r     - . - m     / / � 0 0  l o o p e d _ a u d i o . o      ���� 0 newtitle newTitle��  ��   +  1 2 1 l     ��������  ��  ��   2  3 4 3 l  � 5���� 5 O   � 6 7 6 k   � 8 8  9 : 9 I   ������
�� .miscactvnull��� ��� null��  ��   :  ; < ; I   #�� =��
�� .sysodelanull��� ��� nmbr = m    ���� ��   <  > ? > l  $ $��������  ��  ��   ?  @ A @ l  $ $�� B C��   B 8 2 Open the import file dialog (Shift + Command + I)    C � D D d   O p e n   t h e   i m p o r t   f i l e   d i a l o g   ( S h i f t   +   C o m m a n d   +   I ) A  E F E O   $ � G H G k   ( � I I  J K J l  ( (��������  ��  ��   K  L M L l  ( (��������  ��  ��   M  N O N l  ( (��������  ��  ��   O  P Q P l  ( (�� R S��   R    delete any existing audio    S � T T 4   d e l e t e   a n y   e x i s t i n g   a u d i o Q  U V U l  ( 1 W X Y W I  ( 1�� Z [
�� .prcskprsnull���     ctxt Z m   ( ) \ \ � ] ]  a [ �� ^��
�� 
faal ^ J   * - _ _  `�� ` m   * +��
�� eMdsKcmd��  ��   X #  Select audio file if present    Y � a a :   S e l e c t   a u d i o   f i l e   i f   p r e s e n t V  b c b I  2 7�� d��
�� .sysodelanull��� ��� nmbr d m   2 3 e e ?�      ��   c  f g f l  8 C h i j h I  8 C�� k��
�� .prcskprsnull���     ctxt k l  8 ? l���� l I  8 ?�� m��
�� .prcskcodnull���     **** m m   8 ;���� 3��  ��  ��  ��   i $  This sends a delete keystroke    j � n n <   T h i s   s e n d s   a   d e l e t e   k e y s t r o k e g  o p o I  D I�� q��
�� .sysodelanull��� ��� nmbr q m   D E r r ?�      ��   p  s t s l  J Q u v w u I  J Q�� x��
�� .prcskprsnull���     ctxt x o   J M��
�� 
ret ��   v  go to begining of grid    w � y y , g o   t o   b e g i n i n g   o f   g r i d t  z { z l  R R��������  ��  ��   {  | } | I  R `�� ~ 
�� .prcskprsnull���     ctxt ~ m   R U � � � � �  I  �� ���
�� 
faal � J   V \ � �  � � � m   V Y��
�� eMdsKsft �  ��� � m   Y Z��
�� eMdsKcmd��  ��   }  � � � I  a f�� ���
�� .sysodelanull��� ��� nmbr � m   a b���� ��   �  � � � l  g g��������  ��  ��   �  � � � l  g g�� � ���   � $  Navigate to the target folder    � � � � <   N a v i g a t e   t o   t h e   t a r g e t   f o l d e r �  � � � l  g u � � � � I  g u�� � �
�� .prcskprsnull���     ctxt � m   g j � � � � �  G � �� ���
�� 
faal � J   k q � �  � � � m   k n��
�� eMdsKsft �  ��� � m   n o��
�� eMdsKcmd��  ��   � ) # Opens "Go to Folder" in the dialog    � � � � F   O p e n s   " G o   t o   F o l d e r "   i n   t h e   d i a l o g �  � � � I  v {�� ���
�� .sysodelanull��� ��� nmbr � m   v w���� ��   �  � � � I  | ��� ���
�� .prcskprsnull���     ctxt � o   | }���� 0 targetfolder targetFolder��   �  � � � I  � ��� ���
�� .sysodelanull��� ��� nmbr � m   � ����� ��   �  � � � I  � ��� ���
�� .prcskprsnull���     ctxt � o   � ���
�� 
ret ��   �  � � � l  � � � � � � I  � ��� ���
�� .sysodelanull��� ��� nmbr � m   � ����� ��   � $  Allow folder contents to load    � � � � <   A l l o w   f o l d e r   c o n t e n t s   t o   l o a d �  � � � l  � ���������  ��  ��   �  � � � l  � ��� � ���   � * $ Select the first file in the folder    � � � � H   S e l e c t   t h e   f i r s t   f i l e   i n   t h e   f o l d e r �  � � � l  � � � � � � I  � ��� ���
�� .prcskcodnull���     **** � m   � ����� }��   � 4 . Down Arrow key -- Move focus to the file list    � � � � \   D o w n   A r r o w   k e y   - -   M o v e   f o c u s   t o   t h e   f i l e   l i s t �  � � � I  � ��� ���
�� .sysodelanull��� ��� nmbr � m   � ����� ��   �  � � � l  � � � � � � I  � ��� ���
�� .prcskprsnull���     ctxt � o   � ���
�� 
ret ��   �   Open the selected file    � � � � .   O p e n   t h e   s e l e c t e d   f i l e �  ��� � l  � � � � � � I  � ��� ���
�� .prcskprsnull���     ctxt � o   � ���
�� 
ret ��   � ( " Converts file in case popup shows    � � � � D   C o n v e r t s   f i l e   i n   c a s e   p o p u p   s h o w s��   H m   $ % � ��                                                                                  sevs  alis    \  Macintosh HD               �<�@BD ����System Events.app                                              �����<�@        ����  
 cu             CoreServices  0/:System:Library:CoreServices:System Events.app/  $  S y s t e m   E v e n t s . a p p    M a c i n t o s h   H D  -System/Library/CoreServices/System Events.app   / ��   F  � � � l  � � � � � � I  � ��� ���
�� .sysodelanull��� ��� nmbr � m   � ����� ��   � &   Allow time for the file to load    � � � � @   A l l o w   t i m e   f o r   t h e   f i l e   t o   l o a d �  � � � l  � �����~��  �  �~   �  � � � l  � ��}�|�{�}  �|  �{   �  � � � l  � ��z � ��z   � . ( Handle sample rate dialog if it appears    � � � � P   H a n d l e   s a m p l e   r a t e   d i a l o g   i f   i t   a p p e a r s �  � � � O   � � � � � Z   � � � ��y � � I  � ��x ��w
�x .coredoexnull���     **** � l  � � ��v�u � 6  � � � � � 4   � ��t �
�t 
cwin � m   � ��s�s  � E   � � � � � 1   � ��r
�r 
pnam � m   � � � � � � � 4 C h a n g e   P r o j e c t   S a m p l e   R a t e�v  �u  �w   � k   � � � �  � � � I  � ��q ��p
�q .prcsclicnull��� ��� uiel � n   � � � � � 4   � ��o �
�o 
butT � m   � � � � � � �  C h a n g e   P r o j e c t � 4   � ��n �
�n 
cwin � m   � ��m�m �p   �  ��l � I  � ��k ��j
�k .sysodelanull��� ��� nmbr � m   � ��i�i �j  �l  �y   � l  � � � �  � I  � ��h�g
�h .prcskprsnull���     ctxt o   � ��f
�f 
ret �g   � * $ Confirm if there's any other dialog     � H   C o n f i r m   i f   t h e r e ' s   a n y   o t h e r   d i a l o g � m   � ��                                                                                  sevs  alis    \  Macintosh HD               �<�@BD ����System Events.app                                              �����<�@        ����  
 cu             CoreServices  0/:System:Library:CoreServices:System Events.app/  $  S y s t e m   E v e n t s . a p p    M a c i n t o s h   H D  -System/Library/CoreServices/System Events.app   / ��   �  l  � ��e�d�c�e  �d  �c    l  � ��b	�b   4 . Select the imported region and enable looping   	 �

 \   S e l e c t   t h e   i m p o r t e d   r e g i o n   a n d   e n a b l e   l o o p i n g  O   �> k  =  l �a�a   * $ Ensure the audio region is selected    � H   E n s u r e   t h e   a u d i o   r e g i o n   i s   s e l e c t e d  l  I �`
�` .prcskprsnull���     ctxt m   �  a �_�^
�_ 
faal J  	  �]  m  �\
�\ eMdsKcmd�]  �^   F @ Selects all regions (assuming only the imported file is loaded)    �!! �   S e l e c t s   a l l   r e g i o n s   ( a s s u m i n g   o n l y   t h e   i m p o r t e d   f i l e   i s   l o a d e d ) "#" I �[$�Z
�[ .sysodelanull��� ��� nmbr$ m  �Y�Y �Z  # %&% l �X�W�V�X  �W  �V  & '(' l �U)*�U  ) * $ Trim the end of the selected region   * �++ H   T r i m   t h e   e n d   o f   t h e   s e l e c t e d   r e g i o n( ,-, l !./0. I !�T12
�T .prcskprsnull���     ctxt1 m  33 �44  x2 �S5�R
�S 
faal5 J  66 7�Q7 m  �P
�P eMdsKctl�Q  �R  / > 8 Use this to zoom out to see the entire region on screen   0 �88 p   U s e   t h i s   t o   z o o m   o u t   t o   s e e   t h e   e n t i r e   r e g i o n   o n   s c r e e n- 9:9 I "'�O;�N
�O .sysodelanull��� ��� nmbr; m  "#�M�M �N  : <=< l (/>?@> I (/�LA�K
�L .prcskprsnull���     ctxtA o  (+�J
�J 
ret �K  ?   Confirm changes		   @ �BB $   C o n f i r m   c h a n g e s 	 	= CDC l 00�IEF�I  E - ' Toggle looping for the selected region   F �GG N   T o g g l e   l o o p i n g   f o r   t h e   s e l e c t e d   r e g i o nD HIH l 07JKLJ I 07�HM�G
�H .prcskprsnull���     ctxtM m  03NN �OO  l�G  K 9 3 Press "L" to enable looping on the selected region   L �PP f   P r e s s   " L "   t o   e n a b l e   l o o p i n g   o n   t h e   s e l e c t e d   r e g i o nI Q�FQ I 8=�ER�D
�E .sysodelanull��� ��� nmbrR m  89�C�C �D  �F   m   � �SS�                                                                                  sevs  alis    \  Macintosh HD               �<�@BD ����System Events.app                                              �����<�@        ����  
 cu             CoreServices  0/:System:Library:CoreServices:System Events.app/  $  S y s t e m   E v e n t s . a p p    M a c i n t o s h   H D  -System/Library/CoreServices/System Events.app   / ��   TUT l ??�B�A�@�B  �A  �@  U VWV l ??�?XY�?  X . ( Bounce/export the project (Command + B)   Y �ZZ P   B o u n c e / e x p o r t   t h e   p r o j e c t   ( C o m m a n d   +   B )W [�>[ O  ?�\]\ k  C�^^ _`_ l CNabca I CN�=de
�= .prcskprsnull���     ctxtd m  CFff �gg  be �<h�;
�< 
faalh J  GJii j�:j m  GH�9
�9 eMdsKcmd�:  �;  b   Open the bounce dialog   c �kk .   O p e n   t h e   b o u n c e   d i a l o g` lml I OT�8n�7
�8 .sysodelanull��� ��� nmbrn m  OP�6�6 �7  m opo l U\qrsq I U\�5t�4
�5 .prcskprsnull���     ctxtt o  UX�3
�3 
ret �4  r   Confirm settings   s �uu "   C o n f i r m   s e t t i n g sp vwv I ]b�2x�1
�2 .sysodelanull��� ��� nmbrx m  ]^�0�0 �1  w yzy l cq{|}{ I cq�/~
�/ .prcskprsnull���     ctxt~ m  cf�� ���  g �.��-
�. 
faal� J  gm�� ��� m  gj�,
�, eMdsKsft� ��+� m  jk�*
�* eMdsKcmd�+  �-  |   select target file path   } ��� 0   s e l e c t   t a r g e t   f i l e   p a t hz ��� I rw�)��(
�) .sysodelanull��� ��� nmbr� m  rs�'�' �(  � ��� I x}�&��%
�& .prcskprsnull���     ctxt� o  xy�$�$ 0 savetofolder saveToFolder�%  � ��� I ~��#��"
�# .sysodelanull��� ��� nmbr� m  ~�!�! �"  � ��� l ������ I ��� ��
�  .prcskprsnull���     ctxt� o  ���
� 
ret �  �   Confirm the folder   � ��� &   C o n f i r m   t h e   f o l d e r� ��� I �����
� .sysodelanull��� ��� nmbr� m  ���� �  � ��� l ������  �  �  � ��� l ������  � . ( Change the title in the "Save As" field   � ��� P   C h a n g e   t h e   t i t l e   i n   t h e   " S a v e   A s "   f i e l d� ��� l ������ I �����
� .prcskprsnull���     ctxt� m  ���� ���  a� ���
� 
faal� J  ���� ��� m  ���
� eMdsKcmd�  �  � - ' Select all text in the "Save As" field   � ��� N   S e l e c t   a l l   t e x t   i n   t h e   " S a v e   A s "   f i e l d� ��� I �����
� .sysodelanull��� ��� nmbr� m  ���� ?�      �  � ��� l ������ I �����
� .prcskprsnull���     ctxt� o  ���� 0 newtitle newTitle�  � ( " Type the new title with timestamp   � ��� D   T y p e   t h e   n e w   t i t l e   w i t h   t i m e s t a m p� ��� I �����
� .sysodelanull��� ��� nmbr� m  ���
�
 �  � ��� l ������ I ���	��
�	 .prcskprsnull���     ctxt� o  ���
� 
ret �  � ) # Confirm the title and begin saving   � ��� F   C o n f i r m   t h e   t i t l e   a n d   b e g i n   s a v i n g� ��� l ������  �  �  � ��� l ������  �  �  � �� � l ����������  ��  ��  �   ] m  ?@���                                                                                  sevs  alis    \  Macintosh HD               �<�@BD ����System Events.app                                              �����<�@        ����  
 cu             CoreServices  0/:System:Library:CoreServices:System Events.app/  $  S y s t e m   E v e n t s . a p p    M a c i n t o s h   H D  -System/Library/CoreServices/System Events.app   / ��  �>   7 m    ���                                                                                  EMAG  alis    6  Macintosh HD               �<�@BD ����Logic Pro X.app                                                ������p        ����  
 cu             Applications  /:Applications:Logic Pro X.app/      L o g i c   P r o   X . a p p    M a c i n t o s h   H D  Applications/Logic Pro X.app  / ��  ��  ��   4 ��� l     ��������  ��  ��  � ���� l     ��������  ��  ��  ��       ������ /��  � ��������
�� .aevtoappnull  �   � ****�� 0 targetfolder targetFolder�� 0 savetofolder saveToFolder�� 0 newtitle newTitle� �����������
�� .aevtoappnull  �   � ****� k    ���  ��  ��  *��  3����  ��  ��  �  � & ���� $�� /������� � \������ e������ ��� �������� ����� ���3��Nf��
�� .sysoexecTEXT���     TEXT�� 0 targetfolder targetFolder�� 0 savetofolder saveToFolder�� 0 newtitle newTitle
�� .miscactvnull��� ��� null
�� .sysodelanull��� ��� nmbr
�� 
faal
�� eMdsKcmd
�� .prcskprsnull���     ctxt�� 3
�� .prcskcodnull���     ****
�� 
ret 
�� eMdsKsft�� }
�� 
cwin�  
�� 
pnam
�� .coredoexnull���     ****
�� 
butT
�� .prcsclicnull��� ��� uiel
�� eMdsKctl����j E�O�j E�O�E�O��*j Olj 	O� ����kvl O�j 	Oa j j O�j 	O_ j Oa �a �lvl Olj 	Oa �a �lvl Okj 	O�j Okj 	O_ j Olj 	Oa j Okj 	O_ j O_ j UOlj 	O� ?*a k/a [a ,\Za @1j  *a k/a a /j Okj 	Y 	_ j UO� =a ��kvl Okj 	Oa  �a !kvl Okj 	O_ j Oa "j Okj 	UO� xa #��kvl Olj 	O_ j Okj 	Oa $�a �lvl Okj 	O�j Okj 	O_ j Okj 	Oa %��kvl O�j 	O�j Okj 	O_ j OPUU� ��� � / U s e r s / m a c / P y c h a r m P r o j e c t s / y o u t u b e _ s l e e p _ a u t o m a t i o n / s t a g i n g _ f i l e s / m u s i c� ��� � / U s e r s / m a c / P y c h a r m P r o j e c t s / y o u t u b e _ s l e e p _ a u t o m a t i o n / o u t p u t _ 2 0 2 4 - 1 1 - 0 7 _ 2 2 - 2 3 - 4 1ascr  ��ޭ