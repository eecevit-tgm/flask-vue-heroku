context('GUI Test', () => {


    it('Connection', () => {
        cy.visit('localhost:8080/')
    })

    it('AddUser',() => {
      cy.get('.btn-success').click()
      cy.get('#form-user-input').type("test")
      cy.get('#form-email-input').type("test")
      cy.get('#form-picture-input').type("test")
      cy.get('#user-modal___BV_modal_body_ > .w-100 > .btn-primary').click()
      cy.get('tbody > :nth-child(6) > :nth-child(2)').contains("test")
    })

  it('deleteUser',() =>{
    cy.get(':nth-child(10) > :nth-child(4) > .btn-danger').click()
  })

  it('updateUser', () => {
    cy.get(':nth-child(2) > :nth-child(4) > .btn-warning').click()
    cy.get('#form-user-edit-input').clear()
    cy.get('#form-user-edit-input').type("CypressTest")
    cy.get('#user-update-modal___BV_modal_body_ > .w-100 > .btn-primary').click()

  })

});
