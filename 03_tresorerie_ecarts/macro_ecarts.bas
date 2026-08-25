Attribute VB_Name = "ModuleEcarts"
' ============================================================
'  Macro VBA — Mise en couleur automatique de l'analyse d'ecarts
'  A importer dans Excel : Alt+F11 > Fichier > Importer un fichier > macro_ecarts.bas
'  Puis executer la macro "ColorierEcarts" (Alt+F8).
'  Elle colore la colonne "Statut" de la feuille Budget_Realise :
'    vert  = Favorable, rouge = Defavorable.
'  Auteur : Yvan Akogbeto
' ============================================================
Option Explicit

Sub ColorierEcarts()
    Dim ws As Worksheet
    Dim derniereLigne As Long, i As Long
    Dim colStatut As Long

    Set ws = ThisWorkbook.Worksheets("Budget_Realise")
    colStatut = 7 ' colonne G = Statut

    ' Les donnees commencent ligne 4 (ligne 3 = entetes)
    derniereLigne = ws.Cells(ws.Rows.Count, 1).End(xlUp).Row

    For i = 4 To derniereLigne
        Select Case ws.Cells(i, colStatut).Value
            Case "Favorable"
                ws.Cells(i, colStatut).Interior.Color = RGB(198, 239, 206) ' vert clair
                ws.Cells(i, colStatut).Font.Color = RGB(0, 97, 0)
            Case "Defavorable"
                ws.Cells(i, colStatut).Interior.Color = RGB(255, 199, 206) ' rouge clair
                ws.Cells(i, colStatut).Font.Color = RGB(156, 0, 6)
        End Select
    Next i

    MsgBox "Analyse d'ecarts coloriee : " & (derniereLigne - 3) & " postes traites.", vbInformation
End Sub
