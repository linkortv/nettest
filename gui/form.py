/********************************************************************************
** Form generated from reading UI file 'design.ui'
**
** Created by: Qt User Interface Compiler version 5.12.8
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_DESIGN_H
#define UI_DESIGN_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QComboBox>
#include <QtWidgets/QHBoxLayout>
#include <QtWidgets/QLabel>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QProgressBar>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QVBoxLayout>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_MainWindow
{
public:
    QWidget *centralwidget;
    QVBoxLayout *verticalLayout;
    QLabel *title;
    QLabel *input_label;
    QHBoxLayout *horizontalLayout_2;
    QLineEdit *lineEdit;
    QComboBox *comboBox;
    QProgressBar *progressBar;
    QLabel *status_label;
    QPushButton *start_test;

    void setupUi(QMainWindow *MainWindow)
    {
        if (MainWindow->objectName().isEmpty())
            MainWindow->setObjectName(QString::fromUtf8("MainWindow"));
        QSizePolicy sizePolicy(QSizePolicy::Fixed, QSizePolicy::Preferred);
        sizePolicy.setHorizontalStretch(150);
        sizePolicy.setVerticalStretch(0);
        sizePolicy.setHeightForWidth(MainWindow->sizePolicy().hasHeightForWidth());
        MainWindow->setSizePolicy(sizePolicy);
        MainWindow->setStyleSheet(QString::fromUtf8("background-color: white;"));
        centralwidget = new QWidget(MainWindow);
        centralwidget->setObjectName(QString::fromUtf8("centralwidget"));
        verticalLayout = new QVBoxLayout(centralwidget);
        verticalLayout->setObjectName(QString::fromUtf8("verticalLayout"));
        title = new QLabel(centralwidget);
        title->setObjectName(QString::fromUtf8("title"));
        title->setStyleSheet(QString::fromUtf8("color: #32a5fa;\n"
"font-size: 20px;\n"
"font-weight: bold;"));
        title->setFrameShadow(QFrame::Plain);
        title->setAlignment(Qt::AlignCenter);

        verticalLayout->addWidget(title);

        input_label = new QLabel(centralwidget);
        input_label->setObjectName(QString::fromUtf8("input_label"));
        input_label->setStyleSheet(QString::fromUtf8("font-size: 14px;"));
        input_label->setAlignment(Qt::AlignLeading|Qt::AlignLeft|Qt::AlignVCenter);
        input_label->setIndent(-1);

        verticalLayout->addWidget(input_label, 0, Qt::AlignLeft|Qt::AlignBottom);

        horizontalLayout_2 = new QHBoxLayout();
        horizontalLayout_2->setObjectName(QString::fromUtf8("horizontalLayout_2"));
        lineEdit = new QLineEdit(centralwidget);
        lineEdit->setObjectName(QString::fromUtf8("lineEdit"));
        lineEdit->setMouseTracking(true);
        lineEdit->setLayoutDirection(Qt::LeftToRight);
        lineEdit->setStyleSheet(QString::fromUtf8("width: 150px;\n"
"height: 25px;\n"
"backgrpund-color: white;\n"
"border: 1px solid rgb(190, 187, 187);\n"
"border-radius: 7px;\n"
"padding-left: 5px;"));
        lineEdit->setMaxLength(256);
        lineEdit->setFrame(true);

        horizontalLayout_2->addWidget(lineEdit);

        comboBox = new QComboBox(centralwidget);
        comboBox->addItem(QString());
        comboBox->addItem(QString());
        comboBox->addItem(QString());
        comboBox->setObjectName(QString::fromUtf8("comboBox"));
        comboBox->setEnabled(true);
        comboBox->setStyleSheet(QString::fromUtf8("QComboBox {\n"
"	background-color: white;\n"
"	border: 1px solid rgb(190, 187, 187);\n"
"	height: 25px;\n"
"	border-radius: 7px;\n"
"}\n"
"QComboBox::drop-down {\n"
"\n"
"border-top-right-radius: 3px;\n"
"border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView{\n"
"background-color:  white;\n"
"color: #4f4f4f;\n"
"\n"
"selection-background-color: #4f4f4f;\n"
"selection-color: black;\n"
"}\n"
"\n"
"\n"
""));
        comboBox->setInsertPolicy(QComboBox::InsertAtTop);
        comboBox->setIconSize(QSize(0, 0));
        comboBox->setDuplicatesEnabled(false);
        comboBox->setFrame(true);

        horizontalLayout_2->addWidget(comboBox);


        verticalLayout->addLayout(horizontalLayout_2);

        progressBar = new QProgressBar(centralwidget);
        progressBar->setObjectName(QString::fromUtf8("progressBar"));
        progressBar->setStyleSheet(QString::fromUtf8("QProgressBar {\n"
"	background-color: rgba(198, 198, 198, 233);\n"
"	border-radius: 10px;\n"
"	color: white;\n"
"	text-align: center;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"	border-radius: 10px;\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.63, y2:0.545455, stop:0 rgba(0, 217, 255, 255), stop:1 rgba(50, 165, 250, 255));\n"
"}"));
        progressBar->setValue(24);

        verticalLayout->addWidget(progressBar);

        status_label = new QLabel(centralwidget);
        status_label->setObjectName(QString::fromUtf8("status_label"));
        status_label->setAutoFillBackground(false);
        status_label->setStyleSheet(QString::fromUtf8("margin: 0;\n"
"padding: 0;\n"
"font-size: 13px; "));
        status_label->setAlignment(Qt::AlignCenter);

        verticalLayout->addWidget(status_label, 0, Qt::AlignTop);

        start_test = new QPushButton(centralwidget);
        start_test->setObjectName(QString::fromUtf8("start_test"));
        start_test->setEnabled(true);
        QSizePolicy sizePolicy1(QSizePolicy::Minimum, QSizePolicy::Minimum);
        sizePolicy1.setHorizontalStretch(0);
        sizePolicy1.setVerticalStretch(0);
        sizePolicy1.setHeightForWidth(start_test->sizePolicy().hasHeightForWidth());
        start_test->setSizePolicy(sizePolicy1);
        start_test->setStyleSheet(QString::fromUtf8("#start_test {\n"
"background-color: #32a5fa;\n"
"color: white;\n"
"height: 30px;\n"
"width: 150px;\n"
"border-radius: 10%; }"));
        start_test->setAutoRepeatDelay(300);

        verticalLayout->addWidget(start_test, 0, Qt::AlignHCenter|Qt::AlignTop);

        MainWindow->setCentralWidget(centralwidget);

        retranslateUi(MainWindow);

        QMetaObject::connectSlotsByName(MainWindow);
    } // setupUi

    void retranslateUi(QMainWindow *MainWindow)
    {
        MainWindow->setWindowTitle(QApplication::translate("MainWindow", "MainWindow", nullptr));
        title->setText(QApplication::translate("MainWindow", "Network test", nullptr));
        input_label->setText(QApplication::translate("MainWindow", "\320\222\320\262\320\265\320\264\320\270\321\202\320\265 \320\260\320\264\321\200\320\265\321\201 \320\270\320\273\320\270 \320\262\321\213\320\261\320\265\321\200\320\270\321\202\320\265 \320\270\320\267 \321\201\320\277\320\270\321\201\320\272\320\260", nullptr));
        comboBox->setItemText(0, QApplication::translate("MainWindow", "world of tanks", nullptr));
        comboBox->setItemText(1, QApplication::translate("MainWindow", "world of warships", nullptr));
        comboBox->setItemText(2, QApplication::translate("MainWindow", "valorant", nullptr));

        status_label->setText(QApplication::translate("MainWindow", "Scan network", nullptr));
        start_test->setText(QApplication::translate("MainWindow", "\320\241\321\202\320\260\321\200\321\202", nullptr));
    } // retranslateUi

};

namespace Ui {
    class MainWindow: public Ui_MainWindow {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_DESIGN_H
