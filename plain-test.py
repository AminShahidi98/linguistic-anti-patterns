IfStatement(
    condition=BinaryOperation(
        operandl=MemberReference(
            member=isChecked,
            postfix_operators=[],
            prefix_operators=[],
            qualifier=,
            selectors=[]
            ),
        operandr=Literal(
            postfix_operators=[],
            prefix_operators=[],
            qualifier=None,
            selectors=[],
            value=5
            ),
        operator===
    ),
    else_statement=IfStatement(
        condition=BinaryOperation(
            operandl=MemberReference(
                member=isChecked,
                postfix_operators=[],
                prefix_operators=[],
                qualifier=,
                selectors=[]
                ),
            operandr=Literal(
                postfix_operators=[],
                prefix_operators=[],
                qualifier=None,
                selectors=[],
                value=4
                ),
        operator===
        ),
        else_statement=IfStatement(
            condition=BinaryOperation(
                operandl=MemberReference(
                    member=isChecked,
                    postfix_operators=[],
                    prefix_operators=[],
                    qualifier=,
                    selectors=[]
                    ),
                operandr=Literal(
                    postfix_operators=[],
                    prefix_operators=[],
                    qualifier=None,
                    selectors=[],
                    value=9
                    ),
                operator===
                ),
            else_statement=BlockStatement(
                label=None,
                statements=[
                    ReturnStatement(
                        expression=Literal(
                            postfix_operators=[],
                            prefix_operators=[],
                            qualifier=None,
                            selectors=[],
                            value=0
                            ),
                        label=None
                        )
                    ]
                ),
            label=None,
            then_statement=BlockStatement(
                label=None,
                statements=[
                    ReturnStatement(
                        expression=Literal(
                            postfix_operators=[],
                            prefix_operators=[],
                            qualifier=None,
                            selectors=[],
                            value=464
                            ),
                        label=None
                        )
                    ]
                )
            ),
        label=None,
        then_statement=BlockStatement(
            label=None,
            statements=[
                ReturnStatement(
                    expression=MemberReference(
                        member=isDobed,
                        postfix_operators=[],
                        prefix_operators=[],
                        qualifier=,
                        selectors=[]
                        ),
                    label=None
                    )
                ]
            )
        ),

    label=None,
    then_statement=BlockStatement(
        label=None,
        statements=[
            ReturnStatement(
                expression=Literal(
                    postfix_operators=[],
                    prefix_operators=[],
                    qualifier=None,
                    selectors=[],
                    value=5
                    ),
                label=None
                )
            ]
        )
    )