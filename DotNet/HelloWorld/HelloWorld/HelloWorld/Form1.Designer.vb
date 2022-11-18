<Global.Microsoft.VisualBasic.CompilerServices.DesignerGenerated()>
Partial Class Form1
    Inherits System.Windows.Forms.Form

    'Form overrides dispose to clean up the component list.
    <System.Diagnostics.DebuggerNonUserCode()>
    Protected Overrides Sub Dispose(ByVal disposing As Boolean)
        Try
            If disposing AndAlso components IsNot Nothing Then
                components.Dispose()
            End If
        Finally
            MyBase.Dispose(disposing)
        End Try
    End Sub

    'Required by the Windows Form Designer
    Private components As System.ComponentModel.IContainer

    'NOTE: The following procedure is required by the Windows Form Designer
    'It can be modified using the Windows Form Designer.  
    'Do not modify it using the code editor.
    <System.Diagnostics.DebuggerStepThrough()>
    Private Sub InitializeComponent()
        Me.btnStop = New System.Windows.Forms.Button()
        Me.SuspendLayout()
        '
        'btnStop
        '
        Me.btnStop.BackColor = System.Drawing.SystemColors.ActiveCaption
        Me.btnStop.ForeColor = System.Drawing.SystemColors.ControlText
        Me.btnStop.Location = New System.Drawing.Point(46, 42)
        Me.btnStop.Name = "btnStop"
        Me.btnStop.Size = New System.Drawing.Size(239, 65)
        Me.btnStop.TabIndex = 0
        Me.btnStop.Text = "Press Here"
        Me.btnStop.UseVisualStyleBackColor = False
        '
        'Form1
        '
        Me.AutoScaleDimensions = New System.Drawing.SizeF(8.0!, 20.0!)
        Me.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font
        Me.BackColor = System.Drawing.SystemColors.ActiveBorder
        Me.ClientSize = New System.Drawing.Size(800, 450)
        Me.Controls.Add(Me.btnStop)
        Me.Name = "Form1"
        Me.Text = "Form1"
        Me.ResumeLayout(False)

    End Sub

    Friend WithEvents btnStop As Button
End Class
