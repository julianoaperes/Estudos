///<reference types="cypress" /> 

describe('home', () => {
  it('webapp deve estar on line', () => {
    cy.visit('/')

    cy.title().should('eq', 'Gerencie suas tarefas com Mark L')
  })
})