context('GUI Test', () => {


    it('Connection', () => {
        cy.visit('localhost:8080/')
    })

    it('Genauer User',() => {
      cy.get(':nth-child(4) > table > tbody > tr > :nth-child(1)') == "eecevit"
    })

});
